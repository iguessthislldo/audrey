import json
import uuid

from django.db import models

class Abstract_Tag(models.Model):
    '''Abstract Base class for Tags'''
    name = models.CharField(
        primary_key = True,
        max_length = 256,
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class Tag(Abstract_Tag):
    '''Tag Class'''
    pass

class Meta_Tag(Abstract_Tag):
    '''Tag that defines the name of relationship between a Tagged_Object
    and a Tag.
    '''
    pass

class Tagged_Object(models.Model):
    '''Base class for Objects that are tagged'''

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    def _tag(self, arg):
        if isinstance(arg, str):
            if not self.tagging_set.filter(tag__name = arg).exists():
                self.tagging_set.create(
                    tag = Tag.objects.get_or_create(name = arg)[0],
                )
        elif isinstance(arg, list):
            for i in arg:
                self._tag(i)
        elif isinstance(arg, dict): # Meta_Tag
            for k, v in arg.items():
                meta_tag_name = k.name if isinstance(k, Meta_Tag) else k
                tag_names = None
                if isinstance(v, str):
                    tag_names = [v]
                elif isinstance(v, Tag):
                    tag_names = v.name
                else:
                    raise TypeError()

                # Get Meta Tag
                meta_tag = Meta_Tag.objects.get_or_create(name = meta_tag_name)[0]

                # Apply Subtags
                for _tag_name in tag_names:
                    tag_name = _tag_name.name if isinstance(_tag_name, Tag) else _tag_name
                    if not self.tagging_set.filter(
                        tag__name = tag_name,
                        meta_tag__name = meta_tag_name,
                    ).exists():
                        tag_instance = Tag.objects.get_or_create(
                            name = tag_name
                        )[0]
                        self.tagging_set.create(
                            meta_tag = meta_tag,
                            tag = tag_instance,
                        )
        elif isinstance(arg, Tag):
            if arg._state.adding: # Not in DB
                raise ValueError(
                    'Tag must be saved before it can be used to tag an object'
                )
            Tagging(tag = arg, object = self).save()
        else:
            raise ValueError(
                'Invalid Type for Tagged_Object.tag(): {}'.format(
                    repr(arg)
                )
            )

    def tag(self, *args):
        ''' Takes JSON of lists or actual lists of strings and meta tag dicts
        and applies them to the Tagged_Object. Also takes Tag Objects and
        lists returned by Tagged_Object.tags_objs().
        '''
        if self._state.adding: # Not in DB
            raise ValueError(
                'Tagged_Object must be saved before it can be tagged'
            )
        for arg in args:
            if isinstance(arg, str): # assume it's parsable as JSON
                try:
                    self._tag(json.loads(arg))
                except json.JSONDecodeError:
                    self._tag(arg)
            else:
                self._tag(arg)
                
    def _untag(self, arg):
        if isinstance(arg, str):
            self.tagging_set.filter(tag__name = arg).delete()
        elif isinstance(arg, dict):
            meta_tag_name = list(arg.keys())[0]
            tag_names = list(arg.values())[0]

            # Get Meta Tag
            query = self.meta_tagging_set.filter(
                meta_tag__name = meta_tag_name
            )

            # Apply Subtags
            if query.exists():
                for tag_name in tag_names:
                    query.filter(tag__name = tag_name).delete()
        elif isinstance(arg, list):
            for i in arg:
                self._untag(i)
        elif isinstance(arg, Tag):
            self._untag(arg.name)

    def untag(self, *args):
        '''Takes the same format of arguments as tag(), except it untages
        it from the object (Deletes Taggings). Ignores tags that don't exist
        and tags that are not tagged on this object.
        '''
        for arg in args:
            if isinstance(arg, str): # assume it's parsable as JSON
                try:
                    self._untag(json.loads(arg))
                except json.JSONDecodeError:
                    self._untag(arg)
            else:
                self._untag(arg)
            
    def tags_objs(self):
        '''Return tags on this object as lists and dicts of Tag and Meta_Tag
        instances.
        '''
        rv = []
        meta = {}
        for tagging in self.tagging_set.all():
            if tagging.meta_tag is None:
                rv.append(tagging.tag)
            else:
                if tagging.meta_tag in meta:
                    meta[tagging.meta_tag].append(tagging.tag)
                else:
                    meta[tagging.meta_tag] = [tagging.tag]

        for k, v in meta.items():
            rv.append({k: v})

        return rv

    def tags_str(self):
        '''Return tags on this object as lists and dicts of strings.'''
        l = []
        for i in self.tags_objs():
            if isinstance(i, Tag):
                l.append(i.name)
            else:
                for k, v in i.items():
                    l.append({k.name : [tag.name for tag in v]})
        return l

    def tags_json(self):
        '''Return tags on this object as JSON of self.tags_str()'''
        return json.dumps(self.tags_str())

    def __str__(self):
        return str(self.id)

class Tagging(models.Model):
    tagged_object = models.ForeignKey(
        Tagged_Object,
        on_delete = models.CASCADE
    )

    tag = models.ForeignKey(
        Tag,
        on_delete = models.CASCADE,
    )

    meta_tag = models.ForeignKey(
        Meta_Tag,
        on_delete = models.CASCADE,
        null = True,
    )

    class Meta:
         unique_together = (('tagged_object', 'tag', 'meta_tag'), )


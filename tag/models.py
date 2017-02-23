import json

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
    '''Concrete Main Tag Class'''
    pass

class Meta_Tag(Abstract_Tag):
    '''Tag that defines the name of relationship between a Tagged_Object
    and a Tag.
    '''
    pass

class Tagged_Object(models.Model):
    '''Base class for Objects that are tagged'''

    def _tag(self, arg):
        if isinstance(arg, str):
            if not self.tagging_set.filter(tag__name = arg).exists():
                Tagging(
                    tag = Tag.objects.get_or_create(name = arg)[0],
                    object = self
                ).save()
        elif isinstance(arg, list):
            for i in arg:
                self._tag(i)
        elif isinstance(arg, dict): # Meta_Tag
            meta_tag_name = list(arg.keys())[0]
            tag_names = list(arg.values())[0]

            # Get Meta Tag
            meta_tag = Meta_Tag.objects.get_or_create(name = meta_tag_name)[0]

            # Apply Subtags
            for tag_name in tag_names:
                if not self.meta_tagging_set.filter(
                    tag__name = tag_name,
                    meta_tag__name = meta_tag_name
                ).exists():
                    tag_instance = Tag.objects.get_or_create(
                        name = tag_name
                    )[0]
                    Meta_Tagging(
                        meta_tag = meta_tag,
                        tag = tag_instance,
                        object = self,
                    ).save()
        elif isinstance(arg, Tag):
            if arg._state.adding: # Not in DB
                arg.save()
            Tagging(tag = arg, object = self).save()
        else:
            raise ValueError(
                'Invalid Type for Tagged_Object.tag(): {}'.format(
                    repr(arg)
                )
            )

    def tag(self, *args):
        ''' Takes JSON of lists or actual lists of strings and meta tag dicts
        and applies them to the Tagged_Object. Also takes Tag Objects but not
        Meta_Tag objects.

        Wrapper for Tagged_Object._tag(), and handles json.
        '''
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

    def _tags(self):
        '''Get Tag instances that this object is tagged with'''
        return [i.tag for i in self.tagging_set.all()]

    def _meta_tags(self):
        '''Get Meta_Tag instances that this object is tagged as a dict with
        a list of the sub Tags
        '''
        meta_tags = {}
        for tagging in self.meta_tagging_set.all():
            meta_tag = tagging.meta_tag
            if meta_tag in meta_tags:
                meta_tags[meta_tag].append(tagging.tag)
            else:
                meta_tags.update({
                    meta_tag: [tagging.tag]
                })

        return meta_tags
            
    def tags(self):
        rv = [{i[0].name: [j.name for j in i[1]]} for i in self._meta_tags().items()]
        for i in self._tags():
            rv.append(i.name)
        return rv

    def __str__(self):
        return json.dumps(self.tags())

class Tagging(models.Model):
    '''Relationship between a Tagged_Object and a Tag.'''
    
    tag = models.ForeignKey(
        Tag,
        on_delete = models.CASCADE,
    )

    object = models.ForeignKey(
        Tagged_Object,
        on_delete = models.CASCADE,
    )

    def __str__(self):
        return '"{}" is tagged "{}"'.format(
            str(self.object),
            self.tag.name,
        )

class Meta_Tagging(models.Model):
    '''Relationship between a Tagged_Object, Meta_Tag and Tag.'''

    meta_tag = models.ForeignKey(
        Meta_Tag,
        on_delete = models.CASCADE,
    )

    object = models.ForeignKey(
        Tagged_Object,
        on_delete = models.CASCADE,
    )

    tag = models.ForeignKey(
        Tag,
        on_delete = models.CASCADE,
    )

    def __str__(self):
        return '"{}" is metatagged "{}" with "{}"'.format(
            repr(self.object),
            self.meta_tag.name,
            self.tag.name,
        )
        


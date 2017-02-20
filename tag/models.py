from django.db import models

class Abstract_Tag(models.Model):
    name = models.CharField(
        primary_key = True,
        max_length = 256,
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class Tag(Abstract_Tag):
    pass

class Meta_Tag(Abstract_Tag):
    pass

class Tagged_Object(models.Model):
    def tag(self, *tags):
        tag_instance = None
        for tag in tags:
            if isinstance(tag, Tag):
                if self.tagging_set.filter(tag__name = tag.name):
                    continue
                else:
                    tag_instance = tag
            else:
                if self.tagging_set.filter(tag__name = str(tag)):
                    continue
                else:
                    tag_instance = Tag.objects.get_or_create(
                        name = str(tag)
                    )[0]

            Tagging(tag = tag_instance, object = self).save()

    def untag(self, *tags):
        name = None
        for tag in tags:
            if isinstance(tag, Tag):
                name = tag.name
            else:
                name = str(tag)
            
            self.tagging_set.filter(tag__name = name).delete()
            
    def tags(self):
        return [i.tag for i in self.tagging_set.all()]

    def tag_strs(self):
        return [i.name for i in self.tags()]

    def __str__(self):
        return str(self.tag_strs())

class Tagging(models.Model):
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
        


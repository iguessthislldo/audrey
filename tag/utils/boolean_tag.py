from tag.models import Tag

TRUE_TAG_NAME = '1'
FALSE_TAG_NAME = '0'
BOOLEAN_TAG_DEFAULT_VALUE = False

def get_boolean_tag(value = None):
    if value is None:
        value = BOOLEAN_TAG_DEFAULT_VALUE

    if value:
        return Tag.objects.get_or_create(name=TRUE_TAG_NAME)[0]
    return Tag.objects.get_or_create(name=FALSE_TAG_NAME)[0]
        
def tagging_bool_eval(tagging):
    if tagging.tag_set.filter(name = TRUE_TAG_NAME).exists():
        return True
    if tagging.tag_set.filter(name = FALSE_TAG_NAME).exists():
        return False
    return BOOLEAN_TAG_DEFAULT_VALUE


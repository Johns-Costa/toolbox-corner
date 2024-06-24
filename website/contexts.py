from .models import Category


def categories(request):
    """
    Context processor to add categories to all templates.
    This function retrieves all Category objects from the
    database and returns them in a dictionary. The dictionary
    is added to the context of all templates rendered during
    the request-response cycle, making the categories available
    globally in all templates.
    """
    return {
        'categories': Category.objects.all()
    }

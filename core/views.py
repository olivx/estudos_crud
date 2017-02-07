from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from core.forms import BookForm
from core.models import Books
from django.db.models import Q


# views
def paginate(request, books_list, per_page=3):
    paginator = Paginator(books_list, per_page)
    page = request.GET.get('page')
    try:
        books = paginator.page(page)

    except PageNotAnInteger:
        books = paginator.page(1)

    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    return books


def book_list(request):
    print(request.GET)
    books_list = Books.objects.all()
    books = paginate(request, books_list)
    return render(request, 'books.html', {'book_list': books})


def book_search(request):
    data = {}
    if 'search' in request.GET:
        books_list = Books.objects.filter(Q(author__icontains=request.GET.get('search')) |
                                          Q(title__icontains=request.GET.get('search'))).order_by('title')
        books  = paginate(request, books_list)
        data['html_table'] = render_to_string('partial/book_table.html', {'book_list': books}, request=request)
    return JsonResponse(data)


def book_save_service(request, message, form, template_form):
    data = {}
    template_table = 'partial/book_table.html'
    if request.method == 'POST':
        if form.is_valid():
            form.save()

            book_list = Books.objects.all()
            books = paginate(request, book_list)

            data['success_message'] = message
            data['form_is_valid'] = True
            data['html_table'] = render_to_string(template_name=template_table, context={'book_list': books},
                                                  request=request)
        else:
            data['form_is_valid'] = False
            data['html_form'] = render_to_string(template_name=template_form, context={'form': form},
                                                 request=request)
    else:
        data['html_form'] = render_to_string(template_name=template_form, context={'form': form},
                                             request=request)
    return JsonResponse(data)


def book_save(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
    else:
        form = BookForm()
    return book_save_service(request, 'New book add with successful!',
                             form, 'partial/create_book_form.html')


def book_update(request, pk):
    book = get_object_or_404(Books, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
    else:
        form = BookForm(instance=book)
    return book_save_service(request, 'Update on book is successful!',
                             form, 'partial/update_book_form.html')


def book_delete(request, pk):
    data = {}
    book = get_object_or_404(Books, pk=pk)

    if request.method == 'POST':
        book.delete()

        books_list = Books.objects.all()
        books = paginate(request, books_list)

        data['success_message'] = 'Book delete with success !'
        data['form_is_valid'] = True
        data['html_table'] = render_to_string('partial/book_table.html',
                                              {'book_list': books}, request=request)
    else:
        form = BookForm(instance=book)
        data['html_form'] = render_to_string(template_name='partial/delete_book_form.html', context={'form': form},
                                             request=request)

    return JsonResponse(data)


def contact(request):
    return render(request, 'partial/contact.html', {})

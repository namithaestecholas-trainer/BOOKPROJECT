# from django.shortcuts import render
# from .models import Book

# def book_list(request):

#     # 1. Retrieve all books
#     # books = Book.objects.all()

#     # 2. Retrieve one book using ID
#     # book = Book.objects.get(id=3)
#     # print(book)

#     # 3. Filter books by category
#     # books = Book.objects.filter(category="novel")
#     # print(books)

#     # 4. Exclude books from a category
#     # books = Book.objects.exclude(category="novel")

#     # 5. Order books by title
#     # books = Book.objects.order_by("-title")

#     # 6. Order books by price (descending)
#     # books = Book.objects.order_by("-price")

#     # 7. Count total books
#     total_books = Book.objects.count()

#     # 8. Get the first book
#     # book = Book.objects.first()

#     # 9. Get the last book
#     # book = Book.objects.last()

#     # 10. Filter books with price greater than 500
#     # books = Book.objects.filter(price__gt=300)

#     # 11. Filter books with price less than 500
#     # books = Book.objects.filter(price__lt=300)

#     # 12. Search books containing a word in the title
#     # books = Book.objects.filter(author__icontains="I")

#     # 13. Check whether books exist
#     # result = Book.objects.filter(category="novel").exists()
#     # print(result)

#     # 14. Create a book
#     # Book.objects.create(
#     #     title="Django Basics",
#     #     author="Anu",
#     #     price=600,
#     #     category="Django",
#     #     available=True
#     # )

#     # 15. Update a book
#     # Book.objects.filter(id=1).update(price=700)

#     # 16. Delete a book
#     # Book.objects.filter(id=1).delete()

#     # Default query for displaying all books
#     books = Book.objects.all()
#     print(books)

#     return render(request, "book_list.html", {"books": books,"count":total_books})


# from django.shortcuts import render, redirect, get_object_or_404
# from .models import Book


# # READ - Display all books
# def book_list(request):
#     books = Book.objects.all()
#     count = books.count()

#     return render(request, 'books/book_list.html', {
#         'books': books,
#         'count': count
#     })


# # CREATE - Add a new book
# def book_create(request):
#     if request.method == 'POST':
#         titles = request.POST.get('title')
#         print(titles)
#         author = request.POST.get('author')
#         price = request.POST.get('price')
#         category = request.POST.get('category')
#         available = request.POST.get('available') == 'on'
#         print(available)

#         Book.objects.create(
#             title=titles,
#             author=author,
#             price=price,
#             category=category,
#             available=available
#         )

#         return redirect('book_list')

#     return render(request, 'books/book_form.html')


# # UPDATE - Edit an existing book
# def book_update(request, id):
#     book = get_object_or_404(Book, id=id)
#     print(book)
#     # book = Book.objects.get(id= id)

#     if request.method == 'POST':
#         book.title = request.POST.get('title')
#         book.author = request.POST.get('author')
#         book.price = request.POST.get('price')
#         book.category = request.POST.get('category')
#         book.available = request.POST.get('available') == 'on'
#         book.save()

#         return redirect('book_list')

#     return render(request, 'books/book_form.html', {
#         'book': book
#     })


# # DELETE - Delete a book
# def book_delete(request, id):
#     book = get_object_or_404(Book, id=id)

#     if request.method == 'POST':
#         book.delete()
#         return redirect('book_list')

#     return render(request, 'books/book_confirm_delete.html', {
#         'book': book
#     })


from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm


# READ
def book_list(request):
    books = Book.objects.all()
    count = books.count()

    return render(request, 'book_list.html', {
        'books': books,
        'count': count
    })


# CREATE
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            print(form)
            print(form.cleaned_data)
            Book.objects.create(
                title=form.cleaned_data['title'],
                author=form.cleaned_data['author'],
                price=form.cleaned_data['price'],
                category=form.cleaned_data['category'],
                available=form.cleaned_data['available'],
                image=form.cleaned_data['image']
            )
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'book_form.html', {'form': form})


# UPDATE
def book_update(request, id):
    # book  = Book.objects.get(id=id)
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            book.title = form.cleaned_data['title']
            book.author = form.cleaned_data['author']
            book.price = form.cleaned_data['price']
            book.category = form.cleaned_data['category']
            book.available = form.cleaned_data['available']

            if form.cleaned_data['image']:
                book.image = form.cleaned_data['image']

            book.save()
            return redirect('book_list')
    else:
        form = BookForm(initial={
            'title': book.title,
            'author': book.author,
            'price': book.price,
            'category': book.category,
            'available': book.available
        })
        print(form)

    return render(request, 'book_form.html', {
        'form': form,
        'book': book
    })


# DELETE
def book_delete(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        book.delete()
        return redirect('book_list')

    return render(request, 'book_delete.html', {'book': book})
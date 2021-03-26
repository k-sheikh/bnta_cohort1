function show_new_book_list(books) {
    const book_list_element = document.getElementById('book_list');

    if (books.length == 0) {
        book_list_element.innerHTML = '<p>(No books found. Select an/another author)</p>'
    } else {
        let book_list_items = '';
        books.forEach(function(book) {
            book_list_items += '<li>' + book.title + '</li>\n'
        })
        book_list_element.innerHTML = '<ul>\n' + book_list_items + '</ul>\n'
    }
}

function update_book_list(author_id) {
    if (author_id < 0)
    {
        show_new_book_list([])
    } else {
        var xhr = new XMLHttpRequest();
        xhr.open("GET", "/api/book?author_id=" + author_id.toString());

        xhr.onload = function (evt) {
            if (this.status == 200) {
                var books = JSON.parse(this.responseText);
                show_new_book_list(books);
            } else {
                show_new_book_list([])
            }
        }

        xhr.send();
    }
}


window.onload = (event) => {
    const dropdown = document.getElementById('author_id');
    dropdown.onchange = function(){
        const author_id = dropdown.options[dropdown.selectedIndex].value;
        update_book_list(author_id);
    }
};

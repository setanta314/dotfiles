function bookmark
    python3 ~/.config/fish/functions/bookmark.py 2> /tmp/book_tmp
    cat /tmp/book_tmp | read where
    cd "$where"
    rm /tmp/book_tmp
end

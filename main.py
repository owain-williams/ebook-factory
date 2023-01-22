from ebookfactory import EbookFactory


subject = input("What is the subject of the eBook?: ")
chapters = EbookFactory.get_ebook_chapters(subject)
chapter_dict = EbookFactory.chapters_to_list(chapters)

# write the chapters to a file
with open(f'ebooks/{subject} ebook.txt', 'w') as file:
    for title in chapter_dict:
        file.write(f'Chapter - {title}\n')
        introduction = EbookFactory.get_chapter_introduction(title, subject)
        file.write(introduction)
        content = EbookFactory.get_chapter_content(title, subject)
        file.write(content)
        summary = EbookFactory.summarise_chapter(content, title, subject)
        file.write(summary)
        file.write('\n\n')

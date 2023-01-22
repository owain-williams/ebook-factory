from ebookfactory import EbookFactory

runsingle = False
book_ideas = ('practicing mindfulness',
              'setting up as self employed in the uk')

if not runsingle:
    for idea in book_ideas:
        chapters = EbookFactory.get_ebook_chapters(idea)
        chapter_dict = EbookFactory.chapters_to_list(chapters)

        # write the chapters to a file
        with open(f'ebooks/{idea} ebook.txt', 'w') as file:
            file.write('Chapters:\n')
            for chapter in chapter_dict:
                file.write(f'{chapter}\n')
            for title in chapter_dict:
                file.write(f'Chapter - {title}\n')
                introduction = EbookFactory.get_chapter_introduction(
                    title, idea)
                file.write(introduction)
                content = EbookFactory.get_chapter_content(title, idea)
                file.write(content)
                summary = EbookFactory.summarise_chapter(
                    content, title, idea)
                file.write(summary)
                file.write('\n\n')

if runsingle:

    subject = input("What is the subject of the eBook?: ")
    chapters = EbookFactory.get_ebook_chapters(subject)
    chapter_dict = EbookFactory.chapters_to_list(chapters)

    # write the chapters to a file
    with open(f'ebooks/{subject} ebook.txt', 'w') as file:
        file.write('Chapters:\n')
        for chapter in chapter_dict:
            file.write(f'{chapter}\n')
        for title in chapter_dict:
            file.write(f'Chapter - {title}\n')
            introduction = EbookFactory.get_chapter_introduction(
                title, subject)
            file.write(introduction)
            content = EbookFactory.get_chapter_content(title, subject)
            file.write(content)
            summary = EbookFactory.summarise_chapter(content, title, subject)
            file.write(summary)
            file.write('\n\n')

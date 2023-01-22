import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def get_ebook_chapters(subject: str) -> str:
    """Get the eBook chapters from OpenAI

    Args:
        subject (str): The subject of the eBook

    Returns:
        str: A list of the chapters for the eBook, in one string
    """
    print(f'Getting eBook chapters for {subject}...')
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Give me 12 chapters for an eBook on {subject}.",
        temperature=1.0,
        max_tokens=500,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0
    )
    return response['choices'][0]['text']


def get_chapter_introduction(chapter: str, subject: str) -> str:
    """Get the chapter introduction from OpenAI

    Args:
        chapter (str): The chapter title
        subject (str): The subject of the eBook

    Returns:
        str: 3 to 5 sentences of introduction for the chapter, in the context of the eBook
    """
    print(f'Getting chapter introduction for {chapter}...')
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Give me a 3-5 sentence introduction for a chapter on {chapter}, in a book about {subject}.",
        temperature=1.0,
        max_tokens=500,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0
    )
    return response['choices'][0]['text']


def get_chapter_content(chapter: str, subject: str) -> str:
    """Get the chapter content from OpenAI

    Args:
        chapter (str): The chapter title
        subject (str): The subject of the eBook

    Returns:
        str: 8 to 10 paragraphs of content for the chapter, in the context of the eBook
    """
    print(f'Getting chapter content for {chapter}...')
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Give me 8-10 paragraphs of content for a chapter on {chapter}, in a book about {subject}.",
        temperature=1.0,
        max_tokens=4000,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0
    )
    return response['choices'][0]['text']


def get_chapter_summary(chapter: str, subject: str) -> str:
    """Get the chapter summary from OpenAI

    Args:
        chapter (str): The chapter title
        subject (str): The subject of the eBook

    Returns:
        str: 3 to 5 sentences of summary for the chapter, in the context of the eBook
    """
    print(f'Getting chapter summary for {chapter}...')
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Give me a 3-5 sentence summary for a chapter on {chapter}, in a book about {subject}.",
        temperature=1.0,
        max_tokens=500,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0
    )
    return response['choices'][0]['text']


def summarise_chapter(content: str, chapter: str, subject: str) -> str:
    print(f'Summarising {chapter}...')
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Give me a 3-5 sentence summary of the following in a book about {subject}: {content}",
        temperature=1.0,
        max_tokens=4000,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0
    )
    return response['choices'][0]['text']


def chapters_to_list(chapters: str) -> list:
    """Convert the chapters string to a list of chapter names

    Args:
        chapters (str): The string of chapters to be converted

    Returns:
        list: The formatted list of chapter names
    """
    print(chapters)
    basic_chapter_list = []
    refined_chapter_list = []
    basic_chapter_list = chapters.split('\n')
    # lose the first two items in the list
    basic_chapter_list = basic_chapter_list[2:]
    # in every list item, remove the first word
    for chapter in basic_chapter_list:
        refined_chapter_list.append(chapter.split(' ', 1)[1])

    # chapter_names = list(filter(None, chapter_names))
    print(refined_chapter_list)
    return refined_chapter_list


subject = input("What is the subject of the eBook?: ")
chapters = get_ebook_chapters(subject)
chapter_dict = chapters_to_list(chapters)

# write the chapters to a file
with open(f'ebooks/{subject} ebook.txt', 'w') as file:
    for title in chapter_dict:
        file.write(f'Chapter - {title}\n')
        introduction = get_chapter_introduction(title, subject)
        file.write(introduction)
        content = get_chapter_content(title, subject)
        file.write(content)
        summary = summarise_chapter(content, title, subject)
        file.write(summary)
        file.write('\n\n')

# Siuuuuuu

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ConversationHandler
import csv
import os
from docx import Document
import requests

TOKEN = "TOKEN"
BOT_USERNAME = "@BookSage_Bot"
APIKEY = "API"

GENRE, BOOK_TITLE = range(2)
ADD_BOOK, VIEW_READING_LIST = range(2, 4)
books_list = []  

def fetch_books_by_genre(genre):
    API_URL = f"https://www.googleapis.com/books/v1/volumes?q=subject:{genre}&key={APIKEY}&maxResults=10"
    response = requests.get(API_URL)
    books = response.json().get("items", [])
    return books
async def start_command(update: Update, context):
    await update.message.reply_text(
        "Welcome to BookSage!\n"
        "Happy reading!"
    )
async def book_command(update: Update, context):
    await update.message.reply_text("Please enter a genre:")
    return GENRE
async def genre_handler(update: Update, context):
    genre = update.message.text
    books = fetch_books_by_genre(genre)
    
    with open("books.csv", "w", newline='') as csvfile:
        fieldnames = ["Title", "Author", "Description", "Year Published", "Language"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for book in books:
            volume_info = book['volumeInfo']
            writer.writerow({
                "Title": volume_info.get("title", "N/A"),
                "Author": ", ".join(volume_info.get("authors", [])),
                "Description": volume_info.get("description", "N/A"),
                "Year Published": volume_info.get("publishedDate", "N/A"),
                "Language": volume_info.get("language", "N/A"),
            })
    await update.message.reply_document(document=open("books.csv", 'rb'))
    return ConversationHandler.END
async def preview_command(update: Update, context):
    await update.message.reply_text("Please enter the title of the book for a preview link:")
    return BOOK_TITLE
def fetch_book_preview(title):
    API_URL = f"https://www.googleapis.com/books/v1/volumes?q=intitle:{title}&key={APIKEY}&maxResults=1"
    response = requests.get(API_URL)
    books = response.json().get("items", [])
    if books:
        volume_info = books[0].get('volumeInfo', {})
        return volume_info.get("previewLink", "No preview available")
    return "No preview available"
async def book_title_handler(update: Update, context):
    title = update.message.text
    preview_link = fetch_book_preview(title)
    await update.message.reply_text(f"Preview link for '{title}': {preview_link}")
    return ConversationHandler.END
async def help_command(update: Update, context):
    await update.message.reply_text(
        "BookSage Help:\n\n"
        "Commands you can use:\n"
        "- /start: Welcome message.\n"
        "- /book: Find books by genre.\n"
        "- /preview: Get a preview link for a book.\n"
        "- /help: Show this help message.")
async def list_command(update, context):
    await update.message.reply_text(
        "Choose an option:\n"
        "- /add_book: Add a book\n"
        "- /delete_book: Delete a book\n"
        "- /view_reading_list: View Reading List"  )
def main():
    application = Application.builder().token(TOKEN).build()
    book_conv_handler = ConversationHandler(
        entry_points=[CommandHandler("book", book_command)],
        states={
            GENRE: [MessageHandler(filters.TEXT & ~filters.COMMAND, genre_handler)]
        },
        fallbacks=[], )
    preview_conv_handler = ConversationHandler(
        entry_points=[CommandHandler("preview", preview_command)],
        states={
            BOOK_TITLE: [MessageHandler(filters.TEXT & ~filters.COMMAND, book_title_handler)]
        },
        fallbacks=[], )
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(book_conv_handler)
    application.add_handler(preview_conv_handler)
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("list", list_command))
    
    application.run_polling()

if __name__ == "__main__":
    main()
    
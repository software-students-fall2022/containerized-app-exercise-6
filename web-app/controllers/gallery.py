from flask import Blueprint, render_template

gallery_page = Blueprint( "gallery_page", __name__ )

@gallery_page.route("/")
def display():
    return "hello"


from database.database import (
    execute_query,
    fetch_one,
    fetch_all
)

from services.validation import validate_question

def add_question(
    subject,
    chapter,
    question_text,
    question_type,
    option_a=None,
    option_b=None,
    option_c=None,
    option_d=None,
    correct_option=None,
    marks=1,
    negative_marks=0
):
    valid, message = validate_question(
        subject,
        chapter,
        question_text,
        question_type,
        option_a,
        option_b,
        option_c,
        option_d,
        correct_option,
        marks,
        negative_marks
    )
    if not valid:
        raise ValueError(message)
    cursor = execute_query(
        """
        INSERT INTO questions (
            subject,
            chapter,
            question_text,
            question_type,
            option_a,
            option_b,
            option_c,
            option_d,
            correct_option,
            marks,
            negative_marks
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            subject,
            chapter,
            question_text,
            question_type,
            option_a,
            option_b,
            option_c,
            option_d,
            correct_option,
            marks,
            negative_marks
        )
    )
    return cursor.lastrowid

def get_question(question_id):
    return fetch_one(
        """
        SELECT *
        FROM questions
        WHERE id = ?
        """,
        (question_id,)
    )

def get_all_questions():
    return fetch_all(
        """
        SELECT *
        FROM questions
        ORDER BY id
        """
    )

def search_questions(search_text):
    search_pattern = f"%{search_text}%"
    return fetch_all(
        """
        SELECT *
        FROM questions
        WHERE question_text LIKE ?
           OR subject LIKE ?
           OR chapter LIKE ?
        ORDER BY id
        """,
        (
            search_pattern,
            search_pattern,
            search_pattern
        )
    )

def update_question(
    question_id,
    subject,
    chapter,
    question_text,
    question_type,
    option_a=None,
    option_b=None,
    option_c=None,
    option_d=None,
    correct_option=None,
    marks=1,
    negative_marks=0
):
    valid, message = validate_question(
        subject,
        chapter,
        question_text,
        question_type,
        option_a,
        option_b,
        option_c,
        option_d,
        correct_option,
        marks,
        negative_marks
    )
    if not valid:
        raise ValueError(message)
    cursor = execute_query(
        """
        UPDATE questions
        SET
            subject = ?,
            chapter = ?,
            question_text = ?,
            question_type = ?,
            option_a = ?,
            option_b = ?,
            option_c = ?,
            option_d = ?,
            correct_option = ?,
            marks = ?,
            negative_marks = ?
        WHERE id = ?
        """,
        (
            subject,
            chapter,
            question_text,
            question_type,
            option_a,
            option_b,
            option_c,
            option_d,
            correct_option,
            marks,
            negative_marks,
            question_id
        )
    )
    return cursor.rowcount > 0

def delete_question(question_id):
    cursor = execute_query(
        """
        DELETE FROM questions
        WHERE id = ?
        """,
        (question_id,)
    )
    return cursor.rowcount > 0
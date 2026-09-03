from datetime import datetime
from database.database import (
    execute_query,
    fetch_one,
    fetch_all
)

def create_test(
    title,
    subject,
    duration_minutes,
    total_questions,
    positive_marks=1,
    negative_marks=0,
    start_time=None,
    end_time=None
):
    created_at = datetime.now().isoformat(timespec="seconds")
    cursor = execute_query(
        """
        INSERT INTO tests (
            title,
            subject,
            duration_minutes,
            total_questions,
            positive_marks,
            negative_marks,
            start_time,
            end_time,
            created_at
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            title,
            subject,
            duration_minutes,
            total_questions,
            positive_marks,
            negative_marks,
            start_time,
            end_time,
            created_at
        )
    )
    return cursor.lastrowid

def get_test(test_id):

    return fetch_one(
        """
        SELECT *
        FROM tests
        WHERE id = ?
        """,
        (test_id,)
    )

def get_all_tests():
    return fetch_all(
        """
        SELECT *
        FROM tests
        ORDER BY id
        """
    )

def update_test(
    test_id,
    title,
    subject,
    duration_minutes,
    total_questions,
    positive_marks=1,
    negative_marks=0,
    start_time=None,
    end_time=None
):
    cursor = execute_query(
        """
        UPDATE tests
        SET
            title = ?,
            subject = ?,
            duration_minutes = ?,
            total_questions = ?,
            positive_marks = ?,
            negative_marks = ?,
            start_time = ?,
            end_time = ?
        WHERE id = ?
        """,
        (
            title,
            subject,
            duration_minutes,
            total_questions,
            positive_marks,
            negative_marks,
            start_time,
            end_time,
            test_id
        )
    )
    return cursor.rowcount > 0

def delete_test(test_id):
    cursor = execute_query(
        """
        DELETE FROM tests
        WHERE id = ?
        """,
        (test_id,)
    )
    return cursor.rowcount > 0

def add_question_to_test(
    test_id,
    question_id,
    question_number
):
    cursor = execute_query(
        """
        INSERT INTO test_questions (
            test_id,
            question_id,
            question_number
        )
        VALUES (?, ?, ?)
        """,
        (
            test_id,
            question_id,
            question_number
        )
    )
    return cursor.rowcount > 0

def get_test_questions(test_id):
    return fetch_all(
        """
        SELECT
            q.*,
            tq.question_number

        FROM test_questions tq

        JOIN questions q
            ON tq.question_id = q.id

        WHERE tq.test_id = ?

        ORDER BY tq.question_number
        """,
        (test_id,)
    )

def remove_question_from_test(
    test_id,
    question_id
):
    cursor = execute_query(
        """
        DELETE FROM test_questions
        WHERE test_id = ?
          AND question_id = ?
        """,
        (
            test_id,
            question_id
        )
    )
    return cursor.rowcount > 0
from database.schema import initialize_database

from services.question_service import (
    add_question,
    get_question,
    get_all_questions,
    search_questions,
    update_question,
    delete_question
)

def main():

    initialize_database()

    # CREATE
    question_id = add_question(
        subject="Physics",
        chapter="Electrostatics",
        question_text="What is the SI unit of electric charge?",
        question_type="MCQ",
        option_a="Volt",
        option_b="Coulomb",
        option_c="Ampere",
        option_d="Ohm",
        correct_option="B",
        marks=4,
        negative_marks=1
    )
    print("Created question:", question_id)

    # READ ONE
    question = get_question(question_id)
    print("\nCreated question:")
    print(dict(question))

    # UPDATE
    updated = update_question(
        question_id=question_id,
        subject="Physics",
        chapter="Electrostatics",
        question_text="What is the SI unit of electric charge?",
        question_type="MCQ",
        option_a="Volt",
        option_b="Coulomb",
        option_c="Ampere",
        option_d="Ohm",
        correct_option="B",
        marks=5,
        negative_marks=2
    )

    print("\nUpdated:", updated)

    question = get_question(question_id)

    print("After update:")
    print(dict(question))

    # SEARCH
    results = search_questions("electric")
    print("\nSearch results:")
    for question in results:
        print(
            question["id"],
            question["question_text"]
        )

    # READ ALL
    questions = get_all_questions()
    print("\nTotal questions:", len(questions))

    # DELETE
    deleted = delete_question(question_id)
    print("\nDeleted:", deleted)

    # VERIFY DELETE
    question = get_question(question_id)
    print("Question after deletion:", question)

    print("\n--- VALIDATION TESTS ---")

    try:
        add_question(
            subject="",
            chapter="Electrostatics",
            question_text="Test question",
            question_type="MCQ",
            option_a="A",
            option_b="B",
            option_c="C",
            option_d="D",
            correct_option="A",
            marks=4,
            negative_marks=1
        )

    except ValueError as error:
        print("Caught:", error)

    try:
        add_question(
            subject="Physics",
            chapter="Electrostatics",
            question_text="Test question",
            question_type="MCQ",
            option_a="A",
            option_b="",
            option_c="C",
            option_d="D",
            correct_option="A",
            marks=4,
            negative_marks=1
        )

    except ValueError as error:
        print("Caught:", error)

    try:
        add_question(
            subject="Physics",
            chapter="Electrostatics",
            question_text="Test question",
            question_type="MCQ",
            option_a="A",
            option_b="B",
            option_c="C",
            option_d="D",
            correct_option="X",
            marks=4,
            negative_marks=1
        )

    except ValueError as error:
        print("Caught:", error)

    try:
        add_question(
            subject="Physics",
            chapter="Electrostatics",
            question_text="Test question",
            question_type="MCQ",
            option_a="A",
            option_b="B",
            option_c="C",
            option_d="D",
            correct_option="A",
            marks=-4,
            negative_marks=1
        )

    except ValueError as error:
        print("Caught:", error)

if __name__ == "__main__":
    main()
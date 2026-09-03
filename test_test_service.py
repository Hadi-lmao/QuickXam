from database.schema import initialize_database

from services.question_service import add_question
from services.test_service import (
    create_test,
    get_test,
    get_all_tests,
    update_test,
    delete_test,
    add_question_to_test,
    get_test_questions,
    remove_question_from_test
)


def main():

    initialize_database()

    # =====================================
    # CREATE QUESTIONS
    # =====================================

    q1 = add_question(
        subject="Physics",
        chapter="Electrostatics",
        question_text="What is electric charge?",
        question_type="MCQ",
        option_a="Volt",
        option_b="Coulomb",
        option_c="Ampere",
        option_d="Ohm",
        correct_option="B",
        marks=4,
        negative_marks=1
    )

    q2 = add_question(
        subject="Physics",
        chapter="Electrostatics",
        question_text="What is electric potential?",
        question_type="MCQ",
        option_a="Energy per unit charge",
        option_b="Force",
        option_c="Current",
        option_d="Resistance",
        correct_option="A",
        marks=4,
        negative_marks=1
    )

    print("Created questions:", q1, q2)

    # =====================================
    # CREATE TEST
    # =====================================

    test_id = create_test(
        title="Electrostatics Practice",
        subject="Physics",
        duration_minutes=30,
        total_questions=2,
        positive_marks=4,
        negative_marks=1
    )

    print("\nCreated test:", test_id)

    # =====================================
    # GET TEST
    # =====================================

    test = get_test(test_id)

    print("\nTest:")
    print(dict(test))

    # =====================================
    # ADD QUESTIONS TO TEST
    # =====================================

    print("\nAdding questions...")

    print(
        add_question_to_test(
            test_id,
            q1,
            1
        )
    )

    print(
        add_question_to_test(
            test_id,
            q2,
            2
        )
    )

    # =====================================
    # GET TEST QUESTIONS
    # =====================================

    questions = get_test_questions(test_id)

    print("\nTest questions:")

    for question in questions:

        print(
            question["question_number"],
            question["id"],
            question["question_text"]
        )

    # =====================================
    # UPDATE TEST
    # =====================================

    updated = update_test(
        test_id=test_id,
        title="Electrostatics Full Practice",
        subject="Physics",
        duration_minutes=45,
        total_questions=2,
        positive_marks=4,
        negative_marks=1
    )

    print("\nUpdated:", updated)

    print("Updated test:")
    print(dict(get_test(test_id)))

    # =====================================
    # REMOVE QUESTION
    # =====================================

    removed = remove_question_from_test(
        test_id,
        q1
    )

    print("\nRemoved question:", removed)

    print("\nRemaining questions:")

    questions = get_test_questions(test_id)

    for question in questions:

        print(
            question["question_number"],
            question["question_text"]
        )

    # =====================================
    # ALL TESTS
    # =====================================

    tests = get_all_tests()

    print("\nAll tests:")

    for test in tests:

        print(
            test["id"],
            test["title"]
        )

    # =====================================
    # DELETE TEST
    # =====================================

    deleted = delete_test(test_id)

    print("\nDeleted test:", deleted)

    print(
        "Test after deletion:",
        get_test(test_id)
    )


if __name__ == "__main__":
    main()
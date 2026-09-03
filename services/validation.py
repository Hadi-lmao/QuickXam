VALID_QUESTION_TYPES = {
    "MCQ",
    "SUBJECTIVE"
}


def validate_question(
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
    # -------------------------
    # Basic text validation
    # -------------------------

    if not subject or not subject.strip():
        return False, "Subject cannot be empty."

    if not question_text or not question_text.strip():
        return False, "Question text cannot be empty."

    if not question_type or not question_type.strip():
        return False, "Question type cannot be empty."

    # -------------------------
    # Question type
    # -------------------------

    question_type = question_type.upper()

    if question_type not in VALID_QUESTION_TYPES:
        return False, f"Invalid question type: {question_type}"

    # -------------------------
    # Marks validation
    # -------------------------

    if marks <= 0:
        return False, "Marks must be greater than zero."

    if negative_marks < 0:
        return False, "Negative marks cannot be negative."

    # -------------------------
    # MCQ validation
    # -------------------------

    if question_type == "MCQ":

        options = {
            "A": option_a,
            "B": option_b,
            "C": option_c,
            "D": option_d
        }

        for option_name, option_value in options.items():

            if not option_value or not option_value.strip():
                return False, f"Option {option_name} cannot be empty."

        if not correct_option:
            return False, "Correct option must be specified."

        correct_option = correct_option.upper()

        if correct_option not in options:
            return False, "Correct option must be A, B, C or D."

    # -------------------------
    # Everything valid
    # -------------------------

    return True, ""
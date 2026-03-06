from quick_calc.app import QuickCalcApp


def test_full_user_interaction_addition():
    app = QuickCalcApp()
    app.input_number("5")
    app.choose_operator("+")
    result = app.calculate("3")
    assert result == "8"


def test_clear_resets_display():
    app = QuickCalcApp()
    app.input_number("9")
    app.choose_operator("*")
    app.calculate("2")
    cleared = app.clear()
    assert cleared == "0"
    assert app.display == "0"
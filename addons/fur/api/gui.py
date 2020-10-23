from . import context, state, fmt, config, types


def render_dashboard():
    context.clear(config.CASES_WINDOW_NAME)
    context.print(config.CASES_WINDOW_NAME, fmt.state(state.get()))


def add_quote(case: types.Case, msg: str):
    context.print(f'#{case["num"]}', msg)

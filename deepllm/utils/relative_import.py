import importlib
import inspect
import logging

ASSERTION_MESSAGE = "__init__.py 에서 relative_import()를 호출해주세요."

logger = logging.getLogger(__name__)


def relative_import(*paths: str) -> None:
    """
    제공받은 순서대로 상대경로의 모듈을 임포트합니다.
    """
    assert all(path.startswith(".") for path in paths), "상대 경로는 점(.)으로 시작되어야 합니다."

    current_frame = inspect.currentframe()
    assert current_frame is not None, ASSERTION_MESSAGE
    assert current_frame.f_back is not None, ASSERTION_MESSAGE  # get previous frame
    previous_frame = current_frame.f_back

    module = inspect.getmodule(previous_frame)
    assert module is not None, ASSERTION_MESSAGE

    package = module.__package__
    assert package is not None, ASSERTION_MESSAGE

    for path in paths:
        logger.debug(f"Importing module: {path}")
        importlib.import_module(package + path)

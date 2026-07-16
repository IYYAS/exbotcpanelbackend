from django.test import SimpleTestCase

from whatsapp_service.debug_utils import safe_debug_value


class SafeDebugValueTests(SimpleTestCase):
    def test_safe_debug_value_escapes_emoji_for_ascii_stdout(self):
        value = "Hi 😀 there"
        safe_value = safe_debug_value(value)

        self.assertIn("\\U0001f604", safe_value)
        self.assertNotIn("😀", safe_value)

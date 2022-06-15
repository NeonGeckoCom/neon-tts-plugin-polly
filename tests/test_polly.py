# NEON AI (TM) SOFTWARE, Software Development Kit & Application Development System
#
# Copyright 2008-2021 Neongecko.com Inc. | All Rights Reserved
#
# Notice of License - Duplicating this Notice of License near the start of any file containing
# a derivative of this software is a condition of license for this software.
# Friendly Licensing:
# No charge, open source royalty free use of the Neon AI software source and object is offered for
# educational users, noncommercial enthusiasts, Public Benefit Corporations (and LLCs) and
# Social Purpose Corporations (and LLCs). Developers can contact developers@neon.ai
# For commercial licensing, distribution of derivative works or redistribution please contact licenses@neon.ai
# Distributed on an "AS IS” basis without warranties or conditions of any kind, either express or implied.
# Trademarks of Neongecko: Neon AI(TM), Neon Assist (TM), Neon Communicator(TM), Klat(TM)
# Authors: Guy Daniels, Daniel McKnight, Regina Bloomstine, Elon Gasper, Richard Leeds
#
# Specialized conversational reconveyance options from Conversation Processing Intelligence Corp.
# US Patents 2008-2021: US7424516, US20140161250, US20140177813, US8638908, US8068604, US8553852, US10530923, US10530924
# China Patent: CN102017585  -  Europe Patent: EU2156652  -  Patents Pending

import os
import sys
import unittest
from pprint import pprint

sys.path.append(os.path.join(os.path.dirname(__file__), "res"))
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from neon_tts_plugin_polly import PollyTTS
from neon_tts_plugin_polly.util import get_credentials_from_file


class TestPolly(unittest.TestCase):
    def setUp(self) -> None:
        self.polly = PollyTTS()

    def doCleanups(self) -> None:
        try:
            os.remove(os.path.join(os.path.dirname(__file__), "test.wav"))
        except FileNotFoundError:
            pass
        try:
            self.polly.playback.stop()
            self.polly.playback.join()
        except AttributeError:
            pass
        except Exception:
            pass

    def test_get_setup_credentials(self):
        creds = get_credentials_from_file()
        self.assertIsInstance(creds["aws_access_key_id"], str)
        self.assertIsInstance(creds["aws_secret_access_key"], str)

    def test_get_default_credentials(self):
        creds = get_credentials_from_file("/not/a/file")
        self.assertIsInstance(creds["aws_access_key_id"], str)
        self.assertIsInstance(creds["aws_secret_access_key"], str)

    def test_speak_no_params(self):
        out_file = os.path.join(os.path.dirname(__file__), "test.wav")
        file, _ = self.polly.get_tts("Hello.", out_file)
        self.assertEqual(file, out_file)

    def test_get_voice_english(self):
        voice = self.polly._get_voice("en-us", "female")
        self.assertEqual(voice, "Joanna")

    def test_voices_unicode(self):
        voice = self.polly._get_voice("fr-fr", "female")
        self.assertEqual(voice, "Celine")

    def test_describe_voices(self):
        voices = self.polly.polly.describe_voices()
        languages = {v.get("LanguageName"): v.get("LanguageCode") for v in voices["Voices"]}
        self.assertIsInstance(languages, dict)

    def test_empty_speak(self):
        out_file = os.path.join(os.path.dirname(__file__), "test2.wav")
        file, _ = self.polly.get_tts("</speak>Hello.", out_file)
        self.assertFalse(os.path.isfile(out_file))

    def test_describe_voices(self):
        voices = self.polly.polly.describe_voices()
        pprint(voices)
        languages = {v.get("LanguageName"): v.get("LanguageCode") for v in voices["Voices"]}
        pprint(languages)

    def test_empty_speak(self):
        out_file = os.path.join(os.path.dirname(__file__), "test2.wav")
        file, _ = self.polly.get_tts("</speak>Hello.", out_file)
        self.assertFalse(os.path.isfile(out_file))


if __name__ == '__main__':
    unittest.main()

from .context import joesandbox
import unittest


class ConnectTestSuite(unittest.TestCase):

    def test_joesandbox_recent_analysis(self):
        analysis = joesandbox.JoeSandbox.recent_analysis()
        self.assertEqual(len(analysis), 20, 'Found a total of {0} items in JoeSandbox Analysis page.'.format(len(analysis)))

    def test_joesandbox_analysis(self):
        data = joesandbox.JoeSandbox.get_analysis(joe_id=42887)
        if 'analysis' in data and 'hashes' in data['analysis']:
            self.assertEqual(data['analysis']['hashes']['sha256'],
                             'e7c9b364ffe4ced5bdd8f879a03eee4da14da3481d6c5f263e83dc6ef90f76db',
                             'Hash check for job #42887 mismatched.')


if __name__ == '__main__':
    unittest.main()

import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_with_props(self):
        node = HTMLNode(tag="a", value="Link", props={
                        "href": "https://example.com", "target": "_blank"})
        props_html = node.props_to_html()
        self.assertEqual(
            props_html, ' href="https://example.com" target="_blank"')

    def test_props_to_html_without_props(self):
        node = HTMLNode(tag="p", value="Paragraph")
        self.assertEqual(node.props_to_html(), "")

    def test_to_html_not_implemented(self):
        node = HTMLNode(tag="div", value="Content")
        with self.assertRaises(NotImplementedError):
            node.to_html()


if __name__ == "__main__":
    unittest.main()

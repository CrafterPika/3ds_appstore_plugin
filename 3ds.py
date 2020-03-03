from gui.plugins import basePlugin
from gui.widgets import categoryPage
from gui.widgets import installedCategoryPage
from appstore import Appstore

REPO = "https://crafterpika.github.io/3ds-homebrew/"
LIBGET_DIR = "3ds/appstore/.get/packages"

class Plugin(basePlugin.BasePlugin):
	def __init__(self, app, container):
		basePlugin.BasePlugin.__init__(self, app, "Wii", container)
		self.handler = Appstore("Wii", REPO, LIBGET_DIR)

	def get_pages(self):
		all_frame = categoryPage.CategoryPage(self.app, self.container, self.handler, "3ds - All", self.handler.all)
		tools_frame = categoryPage.CategoryPage(self.app, self.container, self.handler, "3ds - Tools", self.handler.tools)
		emus_frame = categoryPage.CategoryPage(self.app, self.container, self.handler, "3ds - Emus", self.handler.emus)
		games_frame = categoryPage.CategoryPage(self.app, self.container, self.handler, "3ds - Games", self.handler.games)
		misc_frame = categoryPage.CategoryPage(self.app, self.container, self.handler, "3ds - Misc.", self.handler.misc)
		installed_frame = installedCategoryPage.InstalledCategoryPage(self.app, self.container, self.handler, "3ds - Installed", self.handler.all)
		return [all_frame, tools_frame, emus_frame, games_frame, misc_frame, installed_frame]

	def exit(self):
		pass

def setup(app, container):
	return Plugin(app, container)
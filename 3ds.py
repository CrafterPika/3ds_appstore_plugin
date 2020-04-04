from gui.widgets import basePlugin, categoryPage, installedCategoryPage
from appstore import Appstore

CP_REPO = "https://3ds.apps.fortheusers.org/"
LIBGET_DIR = "3ds/appstore/.get/packages"

class Plugin(basePlugin.BasePlugin):
	def __init__(self, app, container):
		basePlugin.BasePlugin.__init__(self, app, "3ds", container)
		self.handler = Appstore("3ds", CP_REPO, LIBGET_DIR)

	def get_pages(self):
		all_frame = categoryPage.CategoryPage(self.app, self.container, self.handler, "3ds - All", self.handler.all)
		tools_frame = categoryPage.CategoryPage(self.app, self.container, self.handler, "3ds - Tools", self.handler.tools)
		emus_frame = categoryPage.CategoryPage(self.app, self.container, self.handler, "3ds - Emus", self.handler.emus)
		games_frame = categoryPage.CategoryPage(self.app, self.container, self.handler, "3ds - Games", self.handler.games)
		advanced_frame = categoryPage.CategoryPage(self.app, self.container, self.handler, "3ds - Advanced", self.handler.advanced)
		misc_frame = categoryPage.CategoryPage(self.app, self.container, self.handler, "3ds - Misc.", self.handler.misc)
		installed_frame = installedCategoryPage.InstalledCategoryPage(self.app, self.container, self.handler, "3ds - Installed", self.handler.all)
		return [all_frame, tools_frame, emus_frame, games_frame, advanced_frame, misc_frame, installed_frame]

	def exit(self):
		pass

def setup(app, container):
	return Plugin(app, container)

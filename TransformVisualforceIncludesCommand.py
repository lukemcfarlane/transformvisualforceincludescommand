import sublime, sublime_plugin, re

class TransformVisualforceIncludesCommand(sublime_plugin.TextCommand):
    def run(self, edit, local_path):
        view = self.view
        viewSize = self.view.size()
        # print("View size is " + str(viewSize))
        fullRegion = sublime.Region(0, viewSize)
        lineRegions = view.lines(fullRegion)
        # print("View contains " + str(len(lineRegions)) + " lines")
        includeRegex = "\s*<apex:includeScript value=\"\{!URLFOR\(\$Resource.(.*), '(.*)'\)\}\"/>"
        patt = re.compile(includeRegex)
        for region in lineRegions :
            lineContents = view.substr(region)
            matcher = patt.match(lineContents)
            if matcher is not None :
                resourceName = matcher.group(1)
                pathName = matcher.group(2)
                # print("Found resource name: " + resourceName)
                # print("Found path name: " + pathName)
                newInclude = "<script type=\"text/javascript\" src=\"" + local_path + "/" + resourceName + ".resource/" + pathName + "\"></script>"
                print(newInclude)


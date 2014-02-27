Transform Visualforce Includes
=======================
A Sublime Text 3 plugin.
-------------------------

When a Visualforce page is in the current view, this command goes through each line and converts all $Resource includes in the format:
	<apex:includeScript value="{!URLFOR($Resource.myResource, 'lib/some_js_file.js')}"/>

Into the format:

	<script type="text/javascript" src="../../../resource-bundles/myResource.resource/lib/some_js_file.js"></script>


Currently, the output is printed in the Sublime console (View -> Show Console) which can be copy/pasted into the correct file. Example use case is creating a Javascript unit test HTML page that can be run locally.

Example keyboard shortcut:

	{
		"keys": ["super+shift+h"],
		"command": "transform_visualforce_includes",
		"args": {
			"local_path": "../../../resource-bundles"
		}
	}


Installation
------------

Copy the following files into a new folder "TransformVisualforceIncludesCommand" inside your Sublime Packages directory:
- TransformVisualforceincludesCommand.py
- Default.sublime-commands

**Note:** to locate your Sublime Packages directory, from within Sublime Text go to the Sublime Text menu -> Preferences -> Browse Packages.


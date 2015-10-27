# pycontainer
# create at 2015/10/23
# autor: qianqians
from pyelement import pyelement
from pyhtmlstyle import pyhtmlstyle

class pycontainer(pyelement):
    def __init__(self, cname, layout, praframe):
        super(pycontainer, self).__init__(cname, layout, praframe)

    def flush(self):
        return "", '''<script language="javascript" type="text/javascript" src="jscripts/tiny_mce/tiny_mce.js"></script>
        <script language="javascript" type="text/javascript">
            tinyMCE.init({
                mode : "specific_textareas",
                theme:"advanced",
                language:"zh-CN",});
        </script>'''
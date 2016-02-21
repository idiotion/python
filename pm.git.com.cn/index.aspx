
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head><title>
	项目管理系统 - Global InfoTech
</title>

    <script type="text/javascript" src="JavaScript/iepngfix_tilebg.js"></script>

    <style type="text/css">
        html, body
        {
            margin: 0px;
            background-repeat: inherit;
            width: 100%;
            height: 100%;
            overflow-x: hidden;
            overflow-y: hidden;
            text-align: center;
            background-image: url(images/login_bg.jpg);
        }
        .padTitle
        {
            padding: 0px 0px 10px 0px;
            height: 32px;
        }
        .padTxt
        {
            padding: 1px 5px 1px 5px;
        }
        .btn
        {
            width: 65px;
            font-size: 10pt;
            cursor: hand;
            background-color: #58A3DC;
            font-family: 宋体;
            height: 22px;
            border: none;
            color: #FFFFFF;
            filter: progid:DXImageTransform.Microsoft.Gradient(GradientType=0, StartColorStr=#9DBCEA, EndColorStr=#58A3DC);
        }
        img, div, a, input
        {
            behavior: url(iepngfix.htc);
        }
    </style>
<link href="App_Themes/SkinFile/Styles.css" type="text/css" rel="stylesheet" /></head>
<body style="background-image: url(images/login_bg.jpg); background-repeat: inherit">
    <form name="form1" method="post" action="index.aspx" id="form1">
<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="/wEPDwUJODU5NzYwNjE2ZBgBBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WAwUIYnRuSW1nVFMFCWJ0bkltZ0JCUwUXTG9naW4xJExvZ2luSW1hZ2VCdXR0b24=" />


<script src="/ScriptResource.axd?d=3EyYNpO2MxC3TLBGrKP5zb1Weey2VbytkfwzajP4F3QHxFdmTDVY8BjOks2d4g1J0&amp;t=634818311345119949" type="text/javascript"></script>
    
    <div style="width: 100%; margin: 0 auto">
    </div>
    <div id="divLogin" style="position: absolute; border: none; width: 729px; height: 375px;
        background-image: url(images/login_pic.png); background-position: center; background-repeat: no-repeat;
        margin-left: auto; margin-right: auto; top: 50%; left: 50%; margin: -187px 0px 0px -365px;">
        <table style="width: 100%; height: 100%;">
            <tr>
                <td align="left" valign="top" style="padding: 50px 0px 0px 195px">
                    
                    <div id="UpdatePanel1">

</div>
                    <table style="width: 500px;" border="0" cellpadding="0" cellspacing="0">
                        
                        <tr style="height: 80%;">
                            <td valign="top" style="text-align: left; padding: 30px 0px 0px 30px">
                                <table cellspacing="0" cellpadding="3" border="0" id="Login1">
	<tr>
		<td><table cellpadding="0" border="0">
			<tr>
				<td class="padTitle" align="left" colspan="2"><font face="宋体" color="Black" size="4"><b><div style='vertical-align:middle;'><img src='images/login_icon.png' alt='工时系统登录' style='width: 32px; height:32px' align='middle'/> 工时系统登录</div></b></font></td>
			</tr><tr>
				<td align="right"><font face="宋体" color="#58A3DC" size="2"><label for="Login1_UserName">用户名:</label></font></td><td><font face="宋体" size="2"><input name="Login1$UserName" type="text" value="@git.com.cn" id="Login1_UserName" class="padTxt" />&nbsp;</font></td>
			</tr><tr>
				<td align="right"><font face="宋体" color="#58A3DC" size="2"><label for="Login1_Password">密码:</label></font></td><td><font face="宋体" size="2"><input name="Login1$Password" type="password" id="Login1_Password" class="padTxt" />&nbsp;</font></td>
			</tr><tr>
				<td align="right" colspan="2"><font face="宋体" size="2"><input type="submit" name="Login1$LoginButton" value="登  录" onclick="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;Login1$LoginButton&quot;, &quot;&quot;, true, &quot;Login1&quot;, &quot;&quot;, false, false))" id="Login1_LoginButton" class="btn" /></font></td>
			</tr><tr>
				<td colspan="2"><font face="宋体" size="2"><a id="Login1_PasswordRecoveryLink" href="Authenticate/PasswordReset.aspx">忘记密码？点击这里</a></font></td>
			</tr>
		</table></td>
	</tr>
</table>
                            </td>
                        </tr>
                        
                    </table>
                </td>
            </tr>
        </table>
        <a href="http://gain.git.com.cn/8thManage/login.jsp" target="_blank" style="text-decoration: none;">
            <div id="blink" style="position: relative; top: -40px; right: -10px">
                新业务管理系统（GAIN）已上线
            </div>
        </a>

        <script language="javascript">
            function changeColor() {
                var color = "#f00|#0f0|#00f|#880|#808|#088|yellow|green|blue|gray";
                color = color.split("|");
                document.getElementById("blink").style.color = color[parseInt(Math.random() * color.length)];
            }
            setInterval("changeColor()", 200); 
        </script>

    </div>
    

<script type="text/javascript">
//<![CDATA[
Sys.Application.initialize();
//]]>
</script>
</form>
</body>

<script type="text/javascript" language="javascript ">
    Sys.WebForms.PageRequestManager.getInstance().add_endRequest(EndRequestHandler);
    function EndRequestHandler(sender, args) {
        if (args.get_error() != undefined) {
            if (args.get_error().message.substring(0, 51) == "Sys.WebForms.PageRequestManagerParserErrorException") {
                window.location.reload();   //出现Session丢失时的错误处理，可以自己定义。
            }
            else {
                alert(args.get_error().message);
                alert("发生错误!原因可能是数据不完整,或网络延迟。");   //其他错误的处理。 
            }
            args.set_errorHandled(true);
        }
    }   
</script>

</html>

<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib uri="http://struts.apache.org/tags-html" prefix="html" %>
<%@ taglib uri="http://struts.apache.org/tags-bean" prefix="bean" %>

<html>
<head>
    <title>Login Page</title>
</head>
<body>
    <html:form action="LoginAction" method="post" styleId="loginForm" >
        <html:errors/>
        <h2 style="color:red";>LOGIN PAGE :-</h2>
        <label for="name" >Name:-<br></label>
        <html:text property="name" styleId="name" size="20"/>
        <html:errors property="name"/>

        <br/><br>

        <label for="mobileNumber">Mobile Number :- <br></label>
        <html:text property="mobileNumber" styleId="mobileNumber" size="20"/>
        <html:errors property="mobileNumber"/>

        <br/><br>

        <label for="email">Email :- <br></label>
        <html:text property="email" styleId="email" size="20"/>
        <html:errors property="email"/>

        <br/><br>

        <html:submit value="Login"/>
    </html:form>
</body>
</html>

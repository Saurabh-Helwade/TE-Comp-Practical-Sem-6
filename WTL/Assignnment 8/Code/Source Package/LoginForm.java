package com.example;

import org.apache.struts.action.ActionForm;

public class LoginForm extends ActionForm {

    private String name;
    private String mobileNumber;
    private String email;

    // getters and setters for name
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    // getters and setters for mobileNumber
    public String getMobileNumber() {
        return mobileNumber;
    }

    public void setMobileNumber(String mobileNumber) {
        this.mobileNumber = mobileNumber;
    }

    // getters and setters for email
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
}

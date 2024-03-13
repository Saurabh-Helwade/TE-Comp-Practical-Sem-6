package com.example;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import org.apache.struts.action.ActionForm;
import org.apache.struts.action.ActionForward;
import org.apache.struts.action.ActionMapping;
import org.apache.struts.action.Action;
import org.apache.struts.action.ActionMessage;
import org.apache.struts.action.ActionMessages;

public class LoginAction extends Action {

    @Override
    public ActionForward execute(ActionMapping mapping, ActionForm form, HttpServletRequest request, HttpServletResponse response) throws Exception {
        LoginForm loginForm = (LoginForm) form;

        // Perform validations
        ActionMessages errors = new ActionMessages();

        if (!ValidationHelper.isValidName(loginForm.getName())) {
            errors.add("name", new ActionMessage("error.name.required"));
        }

        if (!ValidationHelper.isValidMobileNumber(loginForm.getMobileNumber())) {
            errors.add("mobileNumber", new ActionMessage("error.mobileNumber.invalid"));
        }

        if (!ValidationHelper.isValidEmail(loginForm.getEmail())) {
            errors.add("email", new ActionMessage("error.email.invalid"));
        }

        // Check if any value is not entered
        if (loginForm.getName().isEmpty() && loginForm.getMobileNumber().isEmpty() && loginForm.getEmail().isEmpty()) {
            errors.add("allFields", new ActionMessage("error.allFields.required"));
        }

        if (!errors.isEmpty()) {
            saveErrors(request, errors);
            return mapping.findForward("failure");
        } else {
            // Successful login
            return mapping.findForward("success");
        }
    }
}

package com.example;

public class ValidationHelper {

    public static boolean isValidName(String name) {
        // Implement your name validation logic
        return name != null && !name.isEmpty();
    }

    public static boolean isValidMobileNumber(String mobileNumber) {
        // Implement your mobile number validation logic
        return mobileNumber != null && mobileNumber.matches("\\d{10}");
    }

    public static boolean isValidEmail(String email) {
        // Implement your email validation logic
        return email != null && email.matches("[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}");
    }
}

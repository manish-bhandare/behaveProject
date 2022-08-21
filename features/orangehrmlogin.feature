Feature: OrangeHRM Login
  Scenario: Login With valid parameters
    Given Launch chrome
    When Open HRM Homepage
    And Enter username "admin" and password "admin123"
    And Click Login button
    Then Dashboard page
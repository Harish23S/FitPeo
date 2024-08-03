
Feature: Navigate to the FitPeo Homepage

    Scenario: Verify the navigation bars on home page are visible

      Given I go to the site "fitpeo.com"
      Then "Revenue Calculator" should be visible
      Then click the "Revenue Calculator"
      Then current url should be "https://www.fitpeo.com/revenue-calculator"
      Then Set the "Slider" value to "820"
      Then "inputValue" should be visible
      Then Compare with "inputValue" and "Slider"
      Then Set the "inputValue" value to "560"
      Then Compare with "Slider" and "inputValue"
      Then Set the "Slider" value "820"
      Then click the "CPT1"
      Then click the "CPT2"
      Then click the "CPT3"
      Then click the "CPT4"
      Then Compare the "final value" with "$110700"
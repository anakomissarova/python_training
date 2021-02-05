Feature: Contacts
  Scenario Outline: Add new contact
    Given A list of contacts
    And A new contact with <firstname>, <lastname> and <mobile_phone>
    When I add new contact to the list
    Then the new list of contacts is equal to the old list with a new contact added

    Examples:
    |firstname|lastname|mobile_phone |
    |Alice    |Jones   |+75436782341 |
    |Bob      |Smith   |(123)67-89-88|
    |Kira     |        |343 12-23-34 |

  Scenario Outline: Modify contact
    Given A list of contacts
    And a random contact from the list
    And new contact data: <firstname>, <lastname> or <mobile_phone>
    When I edit the contact
    Then the new list of contacts is equal to the old list with modified contact replaced

    Examples:
    |firstname|lastname|mobile_phone|
    |Adam |Simpson|         |
    |     |       |123456789|
    |     |       |         |

  Scenario: Delete contact
    Given A list of contacts
    And a random contact from the list
    When I delete the contact
    Then the new list of contacts is equal to the old list with the contact removed


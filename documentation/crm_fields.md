# Fields Documentation

## Communication and Interaction Tracking

### **has_call_in_queue**
- **Name (Machine):** `has_call_in_queue`
- **Type:** Boolean
- **Description:** Indicates if the lead or contact is currently in the call queue.

### **duration_tracking**

- **Name (Machine):** `duration_tracking`
- **Type:** JSON
- **Description:** Tracks the time spent in various statuses by mapping field IDs to durations (in seconds).

### **activity_ids**

- **Name (Machine):** `activity_ids`

- **Type:** One2many
- **Description:** A list of scheduled activities associated with the record.

### **activity_state**

- **Name (Machine):** `activity_state`
- **Type:** Selection
- **Description:** Represents the current status of activities. Possible values:
  - Overdue: Activity's due date has passed.
  - Today: Activity is due today.
  - Planned: Activity is scheduled for the future.

### **activity_date_deadline**

- **Name (Machine):** `activity_date_deadline`
- **Type:** Date
- **Description:** Specifies the deadline for the next activity.

---

## Campaign Management

### **campaign_id**
- **Name (Machine):** `campaign_id`
- **Type:** Many2one
- **Description:** Associates the record with a specific marketing campaign for tracking purposes.

### **source_id**
- **Name (Machine):** `source_id`
- **Type:** Many2one
- **Description:** Identifies the source of the contact or lead (e.g., search engine, email list).

### **medium_id**
- **Name (Machine):** `medium_id`
- **Type:** Many2one
- **Description:** Indicates the delivery method used, such as email, banner ad, or postcard.

---

## Messaging and Notifications

### **message_ids**
- **Name (Machine):** `message_ids`
- **Type:** One2many
- **Description:** A collection of messages exchanged within the record.

### **message_needaction**
- **Name (Machine):** `message_needaction`
- **Type:** Boolean
- **Description:** Indicates whether there are unread messages requiring action.

### **message_needaction_counter**
- **Name (Machine):** `message_needaction_counter`
- **Type:** Integer
- **Description:** Counts the number of messages that require attention.

### **message_attachment_count**
- **Name (Machine):** `message_attachment_count`
- **Type:** Integer
- **Description:** The total number of attachments associated with the record.

---

## Contact Information

### **phone**
- **Name (Machine):** `phone`
- **Type:** Char
- **Description:** Stores the primary phone number of the contact.

### **mobile**
- **Name (Machine):** `mobile`
- **Type:** Char
- **Description:** Stores the mobile number of the contact.

### **email_from**
- **Name (Machine):** `email_from`
- **Type:** Char
- **Description:** Email address of the contact or lead.

### **website**
- **Name (Machine):** `website`
- **Type:** Char
- **Description:** Website URL of the contact or lead.

---

## Revenue and Metrics

### **expected_revenue**
- **Name (Machine):** `expected_revenue`
- **Type:** Monetary
- **Description:** The expected revenue amount associated with the opportunity.

### **recurring_revenue_monthly**
- **Name (Machine):** `recurring_revenue_monthly`
- **Type:** Monetary
- **Description:** Expected Monthly Recurring Revenue (MRR).

### **sale_amount_total**
- **Name (Machine):** `sale_amount_total`
- **Type:** Monetary
- **Description:** The untaxed total of confirmed sales orders.

---

## Record Lifecycle

### **create_uid**
- **Name (Machine):** `create_uid`
- **Type:** Many2one
- **Description:** The user who created the record.

### **create_date**
- **Name (Machine):** `create_date`
- **Type:** Datetime
- **Description:** The date and time the record was created.

### **write_uid**
- **Name (Machine):** `write_uid`
- **Type:** Many2one
- **Description:** The user who last updated the record.

### **write_date**
- **Name (Machine):** `write_date`
- **Type:** Datetime
- **Description:** The date and time the record was last updated.

---

## Tags and Classification

### **tag_ids**
- **Name (Machine):** `tag_ids`
- **Type:** Many2many
- **Description:** Allows classification of leads/opportunities into categories such as "Training" or "Service."

---

## Localization and Address

### **country_id**
- **Name (Machine):** `country_id`
- **Type:** Many2one
- **Description:** The country associated with the contact or lead.

### **state_id**
- **Name (Machine):** `state_id`
- **Type:** Many2one
- **Description:** The state or region linked to the contact.

### **city**
- **Name (Machine):** `city`
- **Type:** Char
- **Description:** The city associated with the address.

---

## Additional Fields

### **x_studio_origen_lead**
- **Name (Machine):** `x_studio_origen_lead`
- **Type:** Char
- **Description:** Custom field to capture the origin of the lead.

### **x_studio_informacin_extra**
- **Name (Machine):** `x_studio_informacin_extra`
- **Type:** Custom Type
- **Description:** Custom field to store additional information about the lead.

---

This documentation provides an overview of key fields, their purposes, and data types, aiding in understanding and utilizing the data structure effectively.

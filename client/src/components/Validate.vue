<template>

<div class="jumbotron jumbotron-fluid">
  <div class="container">
    <h1 class="display-4">Validator</h1>
    <p class="lead">Submit the information from an application into this form to evaluate whether an applicant is approved, denied, or needs further manual reivew.      </p>
    <p><i>Note: the form currently only accepts U.S. based applicants.</i></p>
  </div>
</div>

<div>
    <form @submit.prevent="handleSubmit">
    <div class="form-row row">
      <div class="form-group col-md-6">
        <label for="name_first">First Name:</label>
        <input
          class="form-control"
          type="text"
          id="name_first"
          v-model="form.name_first"
          placeholder="First Name"
          required
        />
      </div>
  
      <div class="form-group col-md-6">
        <label for="name_last">Last Name:</label>
        <input
          class="form-control"
          type="text"
          id="name_last"
          v-model="form.name_last"
          placeholder="Last Name"
          required
        />
      </div>
      </div>
      <div class="form-group">
        <label for="email">Email Address:</label>
        <input
          class="form-control"
          type="email"
          id="email"
          v-model="form.email"
          placeholder="Email"
          required
        />
      </div>
  
      <div class="form-group">
        <label for="birth_date">Date of Birth:</label>
        <input
          class="form-control"
          type="text"
          id="birth_date"
          v-model="form.birth_date"
          placeholder="YYYY-MM-DD"
          required>
      </div>
      <div class="form-group">
        <label for="document_ssn">Social Security Number:</label>
        <input
          class="form-control"
          type="text"
          id="document_ssn"
          v-model="form.document_ssn"
          pattern="\d{9}"
          placeholder="9-digit SSN"
          required
        />
      </div>
  
      <fieldset>
        <legend class="h3">Address</legend>
  
        <div class="form-group">
          <label for="addressLine1">Line 1:</label>
          <input
            class="form-control"
            type="text"
            id="addressLine1"
            v-model="form.addressLine1"
            placeholder="Address Line 1"
            required
          />
        </div>
  
        <div class="form-group">
          <label for="addressLine2">Line 2:</label>
          <input
            class="form-control"
            type="text"
            id="addressLine2"
            v-model="form.addressLine2"
            placeholder="Address Line 2"
          />
        </div>
  
        <div class="form-row row">
        <div class="form-group col-md-6">
          <label for="city">City:</label>
          <input
            class="form-control"
            type="text"
            id="city"
            v-model="form.city"
            placeholder="City"
            required
          />
        </div>
  
        <div class="form-group col-md-6">
          <label for="state">State:</label>
          <input
            class="form-control"
            type="text"
            id="disabledInput"
            v-model="form.state"
            pattern="[A-Z]{2}"
            placeholder="2-letter state code"
            required
          />
        </div>
        </div>
  
        <div class="form-group">
          <label for="zip_code">Zip Code:</label>
          <input
            class="form-control"
            type="text"
            id="zip_code"
            v-model="form.zip_code"
            pattern="\d{5}"
            placeholder="5-digit Zip Code"
            required
          />
        </div>
  
        <div class="form-group">
          <label for="country">Country:</label>
          <input
            class="form-control"
            type="text"
            id="country"
            v-model="form.country"
            readonly
          />
        </div>
      </fieldset>
  
      <button type="submit" class="btn btn-primary">Submit</button>
      
      <button type="button" @click="clearForm" class="btn btn-warning">Clear Form</button>
    </form>
</div>
  </template>
  
  <script>
  import axios from 'axios';
  export default {
    data() {
      return {
        form: {
          name_first: "",
          name_last: "",
          addressLine1: "",
          addressLine2: "",
          city: "",
          state: "",
          zip_code: "",
          country: "US",
          document_ssn: "",
          email: "",
          birth_date: "",
        },
      };
    },
    methods: {
      async handleSubmit() {
        try {
          const response = await axios.post("http://localhost:5001/validate", this.form, {
              headers: {
                "Content-Type": "application/json",
              },
            });
          let outcome = response.data.outcome
          console.log(response)
          console.log(this.form)
          if (outcome === "Approved") {
              alert(` Thank you, "${response.data.name_first} ${response.data.name_last}", for submitting your application. You have been approved.`);
          } else if (outcome === "Manual Review") {
              alert(`Thank you, "${response.data.name_first} ${response.data.name_last}", for submitting your application. Your application is being reviewed, we will be in touch soon.`);
          } else if (outcome === "Denied") {
              alert(`Sorry "${response.data.name_first} ${response.data.name_last}", your application has been denied.`);
          } else {
              alert(`Whoops, something went wrong. Please submit your information again. 
              Error: "${response.data.error}"`);
          }
  
        } catch (error) {
          alert("An error occurred: " + error.message);
        }
      },
      clearForm() {
          if (confirm('Are you sure you want to clear the form?')) {
          this.form = {
              name_first: "",
              name_last: "",
              addressLine1: "",
              addressLine2: "",
              city: "",
              state: "",
              zip_code: "",
              country: "US",
              document_ssn: "",
              email: "",
              birth_date: "",
          };
      }
        },
    },
  };
  </script>  
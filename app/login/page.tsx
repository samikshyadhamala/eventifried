"use client";
import React from 'react';
import { useRouter } from 'next/navigation';
import { FcGoogle } from "react-icons/fc";
import '../signup/Club_signup.css';
import './Login.css';

const Login = () => {
  const router = useRouter();

const handleAuthSelection = (e: React.ChangeEvent<HTMLSelectElement>) => {
  const selection = e.target.value;
  if (selection === "login") {
    router.push("/login");
  } else if (selection === "signup") {
    router.push("/signup");
  }
};


  return (
    <div className='py-3'>
      <main className="main-content d-flex flex-wrap py-4">
        <div className="image-section">
          <img src="./holifest.jpeg" alt="Event" />
        </div>
        <div className="form-section col-sm-12 col-md-6">
          <h2>Login</h2>
          <p>Create your account</p>
          <div className="form">
            <input
              type="email"
              name="email"
              placeholder="Club Official Email Address"
              required
            />
            <input
              type="password"
              name="password"
              placeholder="Password"
              required
            />

            {/* Dropdown for selecting login or signup */}
            <label htmlFor="authSelect">Choose an option:</label>
            <select id="authSelect" onChange={handleAuthSelection}>
              <option value="">-- Select --</option>
              <option value="login">Login as User</option>
              <option value="signup">Login as Club</option>
            </select>

            <label>
              <input
                type="checkbox"
                name="agreedToTerms"
              />
              I agree to the Terms and Conditions
            </label>

            <button className="flex items-center justify-center gap-3 px-4 py-2 border border-gray-300 rounded-lg shadow-sm hover:bg-gray-100 transition duration-200">
              <FcGoogle className="text-xl" />
              <span className="text-sm font-medium text-gray-700">Sign in with Google</span>
            </button>

            <hr />

            <button type="submit">
              <a href="/">Submit</a>
            </button>
          </div>
        </div>
      </main>
    </div>
  );
};

export default Login;

"use client";
import React, { useEffect, useRef, useState } from 'react';
import './Header.css';
import Link from 'next/link';
import { signOut, useSession } from 'next-auth/react';
// import { signIn, signOut, useSession } from 'next-auth/react';

const Header = () => {
  const [open, setOpen] = useState(false);
  const dropdownRef = useRef<HTMLDivElement>(null);
  const session = useSession()
  const [userExists, setuserExists] = useState(false)

  useEffect(() => {
    setuserExists(!!session.data?.user?.email)
  }, [session?.data])


  useEffect(() => {
    const handleClickOutside = (e: MouseEvent) => {
      // Cast e.target to Node because .contains() expects a Node, not EventTarget
      if (dropdownRef.current && !dropdownRef.current.contains(e.target as Node)) {
        setOpen(false);
      }
    };

    document.addEventListener("mousedown", handleClickOutside);
    return () => {
      document.removeEventListener("mousedown", handleClickOutside);
    };
  }, []);

  return (
    <header className='w-100 px-5'>
      <nav className="navbar flex justify-between items-center py-3">
        <div className="logo-container">
          <a href="#" className="logo text-2xl font-bold">Eventify</a>
        </div>

        <div className="search-container">
          <input type="text" placeholder="Search in site" />
          <button type="submit">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16">
              <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z" />
            </svg>
          </button>
        </div>

        <div className="nav-links flex space-x-8">
          <Link href="/" className='text-white'>Home</Link>
          <Link href="/allevent" className='text-white'>Events</Link>
          <Link href="#" className='text-white'>About</Link>
          <Link href="#" className='text-white'>Contact</Link>
          <Link href="./admin/create-event" className='text-white'>Create Event</Link>
          {userExists &&
            <>

            </>}
        </div>

        <div className="relative">
          {userExists ? <>
            <button
              onClick={() => setOpen(!open)}
              className="w-30 h-30 rounded-full overflow-hidden border-2 border-gray-300 focus:outline-none"
            >
                <img
                  src={session?.data?.user?.image || "/api/placeholder/40/40"}
                  alt="Profile Picture"
                  className="w-full h-full object-cover"
              />
            </button>
          </> : <div className='fc gap-3'>
                <Link href="/login" className='px-3 py-2 button-sec text-decoration-none font-extrabold'>Login</Link>
                <Link href="/signup" className='px-3 py-2 button-pri text-decoration-none'>Signup</Link>
                       
                       {/* authenticate signup */}
                {/* <button
                  onClick={() => {
                  signIn("google", {
                      isAdmin: "asdfasdf"
                    });
                  }}
                  className="px-3 py-2 button-pri text-decoration-none"
                >
                  <span className="text-sm font-medium text-gray-700">Sign In</span>
                </button> */}


          </div>}

          {/* Dropdown Menu */}
          {open && (
            <div ref={dropdownRef} className="absolute right-0 mt-2 w-48 bg-white border border-gray-200 rounded-lg shadow-lg z-50">
              <a href="#" className="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 text-decoration-none" >Profile</a>
              <a href='#' className="block px-4 py-2 text-sm w-full text-gray-700 border-none hover:bg-gray-100 text-decoration-none" onClick={() => {
                signOut({
                  redirect: true,
                  callbackUrl: "/"
                })
              }}>Logout</a>
            </div>
          )}
        </div>
      </nav>
    </header>
  );
};

export default Header;

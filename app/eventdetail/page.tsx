'use client';

import React from 'react';
import './Eventcontainer.css';
import { useParams } from 'next/navigation';
import data from './eventData'; // make sure this path is correct
import ImageComponent from './ImageComponent'; // update if location is different

export default function EventDetails() {
  const { id } = useParams(); // for Next.js App Router (app directory)

  const event = data.find((e) => e.id.toString() === id);

  if (!event) return <p>Loading...</p>;

  return (
    <div className="event-details-container">
      <div className="event-banner-wrapper">
        <ImageComponent imageFile={event.image_file} alt={event.event_name} className="event-banner" />
      </div>

      <div className="event-body">
        <h1 className="event-title">{event.event_name}</h1>
        <p className="event-host">Hosted by: {event.host || 'Placeholder Club'}</p>

        <div className="event-info">
          <p><strong>Date:</strong> {event.start_date}</p>
          <p><strong>Time:</strong> {event.start_time}</p>
          <p><strong>Location:</strong> {event.location}</p>
          <p><strong>Price:</strong> {event.ticket_price}</p>
        </div>

        <div className="event-description">
          <h3>Description</h3>
          <p>{event.description || 'No description provided.'}</p>
        </div>

        <button className="buy-ticket-button">Buy Ticket</button>
      </div>
    </div>
  );
}

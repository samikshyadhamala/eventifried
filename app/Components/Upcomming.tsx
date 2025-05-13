import React from "react";
import styles from './Freeevent.module.css';
import Link from 'next/link';
import ImageComponent from './ImageComponent';
import data from './eventData';

const Upcomming = () => {
  const limitedData = data.slice(0, 8);

  const groupedData = [];
  for (let i = 0; i < limitedData.length; i += 2) {
    groupedData.push(limitedData.slice(i, i + 2));
  }

  return (
    <div className={styles.upcomingSection}>
      <h2 className={styles.sectionTitle}>Upcoming Events</h2>

      <div className={styles.upcomingEventsContainer}>
        {groupedData.map((group, groupIndex) => (
          <div key={groupIndex} className={styles.eventsBlock}>
            {group.map((item) => (
              <Link href={`/event/${item.id}`} key={item.id} className={styles.eventLink}>
                <div className={styles.upcomingEventCard}>
                  <div className={styles.eventTag}>{item.tag}</div>
                  <div className={styles.eventImage}>
                    <ImageComponent imageFile={item.image_file} alt={item.event_name} />
                  </div>
                  <div className={styles.eventDetails}>
                    <h4 className={styles.eventType}>{item.event_name}</h4>
                    <h3 className={styles.eventLocation}>{item.location}</h3>
                    <p className={styles.eventDate}>{item.start_date}</p>
                    {item.ticket_price && <p className={styles.ticketPrice}>{item.ticket_price}</p>}
                  </div>
                </div>
              </Link>
            ))}
          </div>
        ))}
      </div>

      <div className={styles.seeMoreContainer}>
        <Link href="#" className={styles.seeMoreLink}>See more</Link>
      </div>
    </div>
  );
};

export default Upcomming;

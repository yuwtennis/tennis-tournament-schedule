
# Overview

Scrape (_scrape_app_) tournament schedules (_schedule entity_) from various tennis venues (_tournament_facts_spec_).
Schedules then registered (_calendar_service_) to external calendar (e.g google calendar).

# Layered architecture

```
Application Layer : scrape_app
------------------------------------------------------------------------------------------
Domain Layer: tournament_facts_spec as value_obj, schedule as entity & repository
------------------------------------------------------------------------------------------
Infrastructure Layer: calendar as service
```
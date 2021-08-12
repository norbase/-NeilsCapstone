# -NeilsCapstone
# **Capstone Proposal:**

# **Gainz Trackr**

_**Gainz Trackr**_ is the digital fitness journal for those fitness enthusiasts seeking a minimalistic yet, fun approach in app journaling. With _**Gainz Trackr**_, users harness the power of logging in their accomplishments (aka _&#39;gainz&#39;_ 💪🏼) from exercise activities.

**Project Overview**

_**Gainz Trackr**_ is a fun and fitness-minded minimalist&#39;s dream of an app that takes in a user&#39;s weight, goal weight, and provides users the ability to log their exercise sessions by each set and repetition combination. This app will allow the user to view their progress in a familiar and fun display of a status bar mimicking that of _hit points_ (aka _&#39;HP&#39;_ as used in popular video games) and _ranking up_ in the style of the U.S. Army&#39;s current ranking structure (_Private, Private First Class, Specialist… and so forth)_ every time an HP quota is met . I will be using _Django_ for the backend and _Materialize_ for the front end.

**Functionality**

- Allow the user to create a profile:
  - Profile will contain goal weight, current weight, and options to add a _before_ and _after_ picture.
- Allow the user to see _hit points_ status bar via three modes:
  - Daily HP
  - Weekly HP
  - Monthly HP
- Daily data will be shown on a scale of calories consumed vs calories allowed for that day.
- Weekly and monthly will show as a line graph to better track weight over time.

**Data Model**

**Profile**

- User&#39;s name
- (Optional) Before/After Photo
- Current weight
- Goal weight
- User text input of &quot;My Goal is to: \_\_\_\_\_\_\_ &quot;

**Daily Page**

- User (Foreign key to profile)
- Total _Hit Points_ (_HP_) accumulated for the day
- User&#39;s _Rank_ to date
- Exercise Logger:
  - Plus/Minus buttons to add/remove a workout
  - Searchable/_Custom_ form field via user input to search for a workout from dataset or add their own workout of choice if not present in dataset
  - _Repetition Number_ button starting at 0, with the ability to increase/decrease when applicable
  - _Checkbox_ for each exercise/repetition to mark off as complete and transform text of current exercise/repetition to ~~strikethrough~~
  - _Submit_ button when completed for the day

**Weekly Page**

- User (Foreign key to profile)
- Total _Hit Points_ (_HP_) accumulated for the week
- User&#39;s _Rank_ to date
- Current profile _Before_ photo adjacent to the side of week&#39;s end photo

**Monthly Page**

- User (Foreign key to profile)
- Total _Hit Points_ (_HP_) accumulated for the month
- User&#39;s _Rank_ to date
- _Before_ photo adjacent to the side of month&#39;s end photo

    - _First logged month:_
      - _Current_ profile _before_ photo as the Monthly Page&#39;s _Before_ photo
    - _Any logged month after first:_
      - Previous month&#39;s end photo as Monthly Page&#39;s _Before_ photo

**Schedule**

**Week 1**

- Implement database
  - Create profile model
  - create single day model
- Connect routes to views for accessing data:
  - create profile
  - update profile
  - delete profile
  - create single day
  - update single day
  - delete single day

**Week 2**

- Work on HTML templates, establish rough framework
- Begin work on styling via _Materialize_

**Week 3**

- Start working on JavaScript for interaction between front end and backend
- Have a functionable product by end of week 3

**Week 4**

- Last minute bug fixes or style changes (i.e. drag/drop via _hamburger menu style_ icon(s) for each logged exercise set for sorting per user&#39;s preference)
- Establish a domain name to share goldmaster version of webapp
# PayloadReleaseComputation

Given a target at a latitude and longitude, we want to compute at which latitude and longitude we want to conduct an airdrop at given aicraft altitude, aircraft velocity, and wind speed relative to ground. This assumes a parachute deployment mechanism.

Note that we need to integrate with the autopilot to only predict once a straight line flight path is in progress. Using this algorithm prior to aircraft turns can result in invalid predictions.
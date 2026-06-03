class Solution:
    def earliestFinishTime(self, landStartTime: list[int], landDuration: list[int], waterStartTime: list[int], waterDuration: list[int]) -> int:
        def get_min_finish(start1: list[int], dur1: list[int], start2: list[int], dur2: list[int]) -> int:
            # Step 1: Greedily find the earliest possible end timeof the first ride type
            min_first_end = min(s + d for s, d in zip(start1, dur1))

            # Step 2: Find the best second ride to follow up
            return min(max(min_first_end, s) + d for s, d in zip(start2, dur2))

        # Check both schedules and take the absolute minimum finish time
        land_then_water = get_min_finish(landStartTime, landDuration, waterStartTime, waterDuration)
        water_then_land = get_min_finish(waterStartTime, waterDuration, landStartTime, landDuration)

        return min(land_then_water, water_then_land)
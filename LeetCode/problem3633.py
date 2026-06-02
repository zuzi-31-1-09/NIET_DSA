class Solution:
    def earliestFinishTime(self, landStartTime: list[int], landDuration: list[int], waterStartTime: list[int], waterDuration: list[int]) -> int:
        def get_min_finish(start1, dur1, start2, dur2):
            # Step 1: Find the earliest possible time to finish any ride in the first category
            min_first_end = min(s + d for s, d in zip(start1, dur1))

            # Step 2: Find the minimum time to complete the second category ride after that
            return min(max(min_first_end, s) + d for s, d in zip(start2, dur2))

        # Strategy 1: Land first, then Water
        ans1 = get_min_finish(landStartTime, landDuration, waterStartTime, waterDuration)
        # Strategy 2: Water first, then Land
        ans2 = get_min_finish(waterStartTime, waterDuration, landStartTime, landDuration)

        return min(ans1, ans2)
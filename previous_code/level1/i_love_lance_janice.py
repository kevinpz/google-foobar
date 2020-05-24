def solution(str):
    decode_str = [chr(ord("z") - ord(c) + ord("a")) if c.islower() else c for c in str]
    return "".join(decode_str)


if __name__ == "__main__":
    problems = {
        "wrw blf hvv ozhg mrtsg'h vkrhlwv?": "did you see last night's episode?",
        "Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!": "Yeah! I can't believe Lance lost his job at the colony!!"
    }

    for pb, sol in problems.items():
        answer = solution(pb)
        print(answer)
        assert answer == sol

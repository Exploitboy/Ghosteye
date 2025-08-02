def compute_match_score(resume, jd):
    score = 0
    breakdown = {}

    # Skill matching
    matched_skills = set(resume['skills']).intersection(set(jd['skills']))
    skill_score = (len(matched_skills) / len(jd['skills']) * 100) if jd['skills'] else 0
    breakdown['Skills'] = skill_score

    # Experience
    exp_score = min((resume['experience'] / jd['experience']) * 100, 100) if jd['experience'] else 0
    breakdown['Experience'] = exp_score

    # Education
    matched_edu = set(resume['education']).intersection(set(jd['education']))
    edu_score = 100 if matched_edu else 0
    breakdown['Education'] = edu_score

    # Weighted total score
    total = 0.4 * skill_score + 0.4 * exp_score + 0.2 * edu_score

    return {
        'total_score': total,
        'breakdown': breakdown
    }
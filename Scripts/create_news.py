import random
import datetime
import requests

from datetime import date
def generate_news_data(
        title: str,
        section: int,
        person: int,
        tag: int,
        importancy: int,
        x: int
):
    return {
            'ID': 0,
            'CreateDate': datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
            'CreateUserID': 0,
            'Localizations': {
                'en': {
                    'ID': 1,
                    'CreateDate': datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
                    'CreateUserID': 0,
                    'LanguageID': 1,
                    'IsCustomSeoTitle': False,
                    'IsCustomSeoDescription': False,
                    'SeoTitle': 'Script News For Life',
                    'SeoDescription': 'SeoText',
                    'Title': f'ru {title} {importancy}',
                    'TitleForSocialNetworks': 'ScriptNewsForSN',
                    'Description': None,
                    "FullText": "<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ac massa ut tellus dictum porttitor. Sed sit amet tellus placerat, egestas sapien non, maximus risus. Nulla suscipit lacus eu nibh feugiat, sed euismod justo tincidunt. Quisque feugiat orci sit amet lectus rutrum semper. Curabitur non luctus nulla. Nulla sed enim in turpis congue feugiat sed sit amet urna. Pellentesque velit odio, interdum quis leo sit amet, aliquam condimentum lectus. Nullam feugiat hendrerit efficitur. In non magna augue. Nam viverra nunc massa, eu dignissim nisl hendrerit quis. Etiam est purus, lobortis in ultrices in, consectetur a metus. Donec vel consectetur felis, ac imperdiet diam.</p>\n<p>Vestibulum maximus facilisis augue quis suscipit. Nam dolor ante, elementum sed venenatis a, pharetra ac justo. Pellentesque id dolor a nibh pellentesque aliquet. Nullam a dui feugiat, bibendum odio nec, pellentesque est. Aliquam eget magna sit amet leo aliquet ultricies. Nulla a pellentesque metus. Nulla cursus leo a erat sollicitudin, non auctor orci eleifend. Vivamus sollicitudin magna vitae dui rhoncus congue. Duis eu diam nisi. Aenean tempor euismod ante sed blandit. Nam vulputate vestibulum arcu, ut finibus lacus gravida quis. Morbi quis risus hendrerit augue efficitur luctus. Aliquam rutrum a sapien bibendum eleifend.</p>\n<p>Etiam vestibulum dui et ullamcorper interdum. Sed sagittis lorem in odio faucibus, at venenatis arcu luctus. Donec hendrerit accumsan lacus, ac iaculis diam bibendum et. Etiam vitae condimentum lectus. Etiam et mi sed est dapibus molestie sit amet non risus. Nullam vehicula nibh nisi, ac pharetra ante gravida sed. Nullam tortor orci, porta in sem non, interdum faucibus massa. Nulla auctor nulla dolor, eget cursus risus pharetra rutrum. Duis augue leo, iaculis et imperdiet a, bibendum eleifend ante. Curabitur efficitur sed dui eget laoreet. Donec nec blandit quam. In quis hendrerit libero, ut rhoncus ipsum. Donec molestie diam at nunc dignissim, in tempor est ullamcorper. Sed nec volutpat nisi, ac vehicula magna.</p>\n<p>Sed sodales, lacus ut mollis varius, lacus diam varius tortor, vel bibendum sem orci sed nisl. Proin a massa posuere, vulputate diam sit amet, venenatis orci. Ut cursus, est quis luctus elementum, felis enim laoreet sapien, sed malesuada sapien nunc ut ipsum. Nunc leo lectus, eleifend ut congue vitae, auctor a sapien. Vivamus sagittis, tortor at porttitor lacinia, mi mi eleifend dui, ac faucibus turpis erat at mauris. Quisque et libero at massa semper elementum nec sit amet lorem. Suspendisse sed laoreet dui, vitae scelerisque mauris. Aliquam fermentum eros nec metus sagittis, eu mattis risus finibus. Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>",
                    'CanonicalLanguageKey': "en",
                    'ViewCount': 0
                },
            },
            'SectionID': 5,
            'ImportanceID': 1,
            'DomainID': 1,
            'UpdateDate': datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
            'PublishDate': datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
            'IsUpdated': False,
             'PseudoSectionID': 5,
            'IsPublished': True,
            'CodeName': '',
            'IsCustomCodeName': False,
            'IsUrlLocked': False,
            'MainImage': {
                'ID': 0,
                'CreateDate': datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
                'CreateUserID': 0,
                'Localizations': {},
                'Formats': [],
            },
            'ViewCount': 0,
            'AuthorIDs': [
            13,
            12
            ],
            'PersonIDs': [1],
            'TagIDs': [],
            'FlagIDs': [],
            'GalleryImages': [],
        }

cookies = {
    'Travel.Media.Admin': 'CfDJ8N5HcILLmzRGsVngPlKbLDqECl5S7LemkC2nhIFCmaVTOkYSy8g7lKS3M19tmdOagCO_tgmT2Sr9xVZN5vXl-W5zZFX7hzifKQPoXewGuac_Tqp29WyOrlhvyEWw6Q7tmvYfoq99K8pGweyDWXgiVO8IeMcbQMC2NI2_C9b_HSM6MvF5MB8-izWLnprqcSyyzc7csCEOmMc6xfkM4ivccUIJgHnPXIhDo2111Qz4GRea8v6IzsoC-mv1nhrpzEwZUSish6MieUo-DlVfaOR__qMOHnBhM-M-8YzPi6ijrAtiyDBon_LiwSdTsDwULHRNLCBQRrBpvYICKYzBMeWYosZr7X6b-oB1l5I289trrufJ1TrdVWOyDm_aoJoHrLelOL61WnkH7ZQdhERGvgNtgMlOU9XPmuUW9dgI0rNoUR-6lzQikp5DN_qicmrq8cSrE8jyoUXiUaN7OVXchidx00_tyFIzC3sIBqCP_r9oCPLNzS19MB56nC35zMF3_X7OBzukHsbHwYvpq7ghwoI4dQeGm1vtTs0ZA4482fUuDr420Nr_I-Rxwu_vXPwVe53_NEEMYI8G4uWRg7X-pe3E3aldhPqG8uWb75c5qw6I7J_8qpSaEB0cYja9xvEK_7qX71VQ3WG4hfefwgDVxA_p28F-DEdgLPh8B-kw_cYyGE9N'
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'uk,uk-UA;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    'Origin': 'https://admin.travelwise.click',
    'Pragma': 'no-cache',
    'Referer': 'https://admin.travelwise.click/news?updateDateFrom=2024-06-06&updateDateTo=2024-06-06T23%3A59%3A59&includeCompletedActions=true&sort=UpdateDateDescending&page=1&total=0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}

for x in range(1):

    response = requests.post(
        'https://admin.travelwise.click/api/media/News',
        cookies=cookies,
        headers=headers,
        json=generate_news_data(
            x=x,
            title=f'News-{x}',
            section=13,
            tag=random.randint(1,1),
            person=random.randint(1,2),
            importancy=random.randint(1,3)

        ),
        verify=True,
    )
    print(response.status_code)
    print(response.text)
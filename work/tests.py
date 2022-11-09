import re

from selenium.webdriver import Keys

from core import fixtures
from core.constant import REL_TYPE_COMMENT_AUTHOR, REL_TYPE_COMMENT_ADDRESSEE, REL_TYPE_COMMENT_DATE, \
    REL_TYPE_COMMENT_DESTINATION, REL_TYPE_COMMENT_ROUTE, REL_TYPE_COMMENT_ORIGIN, REL_TYPE_COMMENT_REFERS_TO, \
    REL_TYPE_PEOPLE_MENTIONED_IN_WORK
from siteedit2.utils.test_utils import EmloSeleniumTestCase, FieldValTester
from uploader.models import Iso639LanguageCode
from work.models import CofkUnionWork


def wait_jquery_ready(selenium):
    return selenium.execute_script('return jQuery.active == 0')


class WorkFormTests(EmloSeleniumTestCase):

    def get_id_by_url_pattern(self, re_pattern):
        iwork_id = re.findall(re_pattern, self.selenium.current_url)
        self.assertTrue(iwork_id)
        iwork_id = iwork_id[0]
        return iwork_id

    def test_corr__create(self):
        self.goto_vname('work:corr_form')

        # fill form
        self.find_element_by_css('#id_author_comment-0-comment').send_keys('xxxxxx')
        field_val_tester = FieldValTester(self, [
            ('authors_as_marked', 'akdjalksdj'),
            ('authors_inferred', 1),
            ('addressees_uncertain', 1),
        ])
        field_val_tester.fill()

        self.click_submit()

        # assert work object
        iwork_id = self.get_id_by_url_pattern(r'/work/form/corr/(\d+)')
        work = CofkUnionWork.objects.filter(iwork_id=iwork_id).first()
        self.assertIsNotNone(work)
        self.assertGreater(work.cofkworkcommentmap_set.filter(relationship_type=REL_TYPE_COMMENT_AUTHOR)
                           .count(), 0)
        field_val_tester.assert_all(work)

        # unchanged field
        self.assertEqual(work.authors_uncertain, 0)
        self.assertEqual(work.addressees_inferred, 0)
        self.assertEqual(work.cofkworkcommentmap_set.filter(relationship_type=REL_TYPE_COMMENT_ADDRESSEE)
                         .count(), 0)

    def test_switch_tab_without_save(self):
        org_size = CofkUnionWork.objects.count()

        def _assert_url_case(url_endswith):
            self.assertTrue(self.selenium.current_url.endswith(url_endswith))

            # should have not CofkUnionWork created after change tab
            self.assertEqual(CofkUnionWork.objects.count(), org_size)

        self.goto_vname('work:corr_form')
        _assert_url_case('/work/form/corr/')

        self.goto_vname('work:dates_form')
        _assert_url_case('/work/form/dates/')

        self.goto_vname('work:places_form')
        _assert_url_case('/work/form/places/')

        self.goto_vname('work:details_form')
        _assert_url_case('/work/form/details/')

    def test_detes__create(self):
        self.goto_vname('work:dates_form')

        # fill form
        field_val_tester = FieldValTester(self, [
            ('date_of_work_as_marked', 'akdjalksdj'),
            ('date_of_work_std_day', 12),
            ('date_of_work_std_year', 2020),
            ('date_of_work_std_is_range', 1),
            ('date_of_work_uncertain', 1),
            ('date_of_work_std_month', 8),
        ])
        field_val_tester.fill()
        self.find_element_by_css('#id_date_comment-0-comment').send_keys('xxxxxx')

        self.click_submit()

        # assert work object
        iwork_id = self.get_id_by_url_pattern(r'/work/form/dates/(\d+)')
        work = CofkUnionWork.objects.filter(iwork_id=iwork_id).first()
        self.assertIsNotNone(work)
        self.assertGreater(work.cofkworkcommentmap_set.filter(relationship_type=REL_TYPE_COMMENT_DATE)
                           .count(), 0)
        field_val_tester.assert_all(work)

        # unchanged field
        self.assertEqual(work.date_of_work_inferred, 0)
        self.assertEqual(work.date_of_work_approx, 0)

    def test_places__create(self):
        self.goto_vname('work:places_form')
        field_val_tester = FieldValTester(self, [
            ('origin_as_marked', 'akdjalksdj'),
            ('origin_uncertain', 1),
        ])
        field_val_tester.fill()
        self.find_element_by_css('#id_destination_comment-0-comment').send_keys('xxxxxx')
        self.find_element_by_css('#id_route_comment-0-comment').send_keys('xxxxxx')

        self.click_submit()

        # assert work object
        iwork_id = self.get_id_by_url_pattern(r'/work/form/places/(\d+)')
        work = CofkUnionWork.objects.filter(iwork_id=iwork_id).first()
        self.assertIsNotNone(work)
        field_val_tester.assert_all(work)

        # assert comment
        self.assertGreater(work.cofkworkcommentmap_set.filter(relationship_type=REL_TYPE_COMMENT_DESTINATION)
                           .count(), 0)
        self.assertGreater(work.cofkworkcommentmap_set.filter(relationship_type=REL_TYPE_COMMENT_ROUTE)
                           .count(), 0)
        self.assertEqual(work.cofkworkcommentmap_set.count(), 2)

        # unchanged field
        self.assertEqual(work.destination_as_marked, '')
        self.assertEqual(work.origin_inferred, 0)
        self.assertEqual(work.destination_inferred, 0)
        self.assertEqual(work.destination_uncertain, 0)
        self.assertEqual(work.cofkworkcommentmap_set.filter(relationship_type=REL_TYPE_COMMENT_ORIGIN)
                         .count(), 0)

    def test_details__create(self):
        for lang_dict in [fixtures.lang_dict_eng, fixtures.lang_dict_ara]:
            lang = Iso639LanguageCode(**lang_dict)
            lang.save()

        self.goto_vname('work:details_form')

        input_lang_list = {'English', 'Arabic'}
        field_val_tester = FieldValTester(self, [
            ('editors_notes', 'akdjalksdj'),
            ('incipit', 'aaa'),
            ('ps', 'kjs'),
            ('keywords', 'xxxx'),
        ])
        field_val_tester.fill()
        self.find_element_by_css('#id_people_comment-0-comment').send_keys('xxxxxx')

        # select language
        lang_ele = self.find_element_by_css('#id_new_language')
        for lang in input_lang_list:
            lang_ele.send_keys(lang)
            lang_ele.send_keys(Keys.ESCAPE)
            self.find_element_by_css('button.lang_add_btn').click()

        self.click_submit()

        # assert work object
        iwork_id = self.get_id_by_url_pattern(r'/work/form/details/(\d+)')
        work = CofkUnionWork.objects.filter(iwork_id=iwork_id).first()
        self.assertIsNotNone(work)
        field_val_tester.assert_all(work)
        self.assertEqual(work.cofkworkcommentmap_set.filter(relationship_type=REL_TYPE_PEOPLE_MENTIONED_IN_WORK)
                         .count(), 1)
        self.assertEqual(work.language_set.count(), 2)
        self.assertSetEqual(
            {l.language_code.language_name for l in work.language_set.iterator()},
            input_lang_list
        )

        # unchanged field
        self.assertEqual(work.accession_code, '')
        self.assertEqual(work.explicit, '')
        self.assertEqual(work.cofkworkcommentmap_set.filter(relationship_type=REL_TYPE_COMMENT_REFERS_TO)
                         .count(), 0)
